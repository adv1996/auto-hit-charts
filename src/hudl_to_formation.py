import argparse, csv, json

#TODO pandas?

def ParseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename",  help="name of file containing HUDL data")
    #TODO add output arg
    args = parser.parse_args()
    return args

def ReadCSVFile(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def AddNewAction(action):
    #array of objects with just the one field idx 21
    return { action : 1 }

def AddNewOffConcept(concept, playtype):
    #Concept is just field idx 23, + run, pass, total
    offConcept={}
    offConcept["offConcept"] = concept
    offConcept["total"] = 1
    if playtype == "pass":
        offConcept["pass"] = 1
        offConcept["run"] = 0
    else:
        offConcept["pass"] = 0
        offConcept["run"] = 1
    return offConcept

def AddNewOffForm(row):
    #offForm, pass, run, total, offConcepts [], actions []
    offForm={}
    offForm["offForm"] = row[11]
    offForm["total"] = 1
    if row[19] == "Pass":
        offForm["pass"] = 1
        offForm["run"] = 0
    else:
        offForm["run"] = 1
        offForm["pass"] = 0
    offConcepts=[]
    offConcepts.append(AddNewOffConcept(row[23], row[19]))
    offForm["offConcepts"] = offConcepts
    actions=[]
    actions.append(AddNewAction(row[21]))
    offForm["actions"] = actions
    return offForm

def UpdateOffForm(row, offForm):
    offForm["total"] += 1
    if row[19] == "Pass":
        offForm["pass"] += 1
    else:
        offForm["run"] += 1

    Found = False
    for oc in offForm["offConcepts"]:
        if row[23] == oc["offConcept"]:
            oc["total"] += 1
            if row[19] == "Pass":
                oc["pass"] += 1
            else:
                oc["run"] += 1
            Found = True
            break
    if not Found:
        offForm["offConcepts"].append(AddNewOffConcept(row[23], row[19]))

    #TODO reformat actions
    """
    Found=False
    for a in offForm["actions"]:
        if row[21] in a:
            offForm["actions"][row[21]] += 1
    if not Found:
        offForm["actions"].append(AddNewAction(row[21]))
    """

def AddNewFormShell(row):
    formShell={}
    formShell["formShell"] = row[16]
    formShell["totalPlays"] = 1
    if row[19] == "Pass":
        formShell["pass"] = 1
        formShell["run"] = 0
    elif row[19] == "Run":
        formShell["pass"] = 0
        formShell["run"] = 1
    else:
        formShell["pass"] = 0
        formShell["run"] = 0
        #TODO change
        formShell["unknown"] = 1
    offForms=[]
    offForms.append(AddNewOffForm(row))
    formShell["offForms"] = offForms
    return formShell

def UpdateFormShell(row, formShell):
    formShell["totalPlays"] += 1
    if row[19] == "Pass":
        formShell["pass"] += 1
    elif row[19] == "Run":
        formShell["run"] += 1
    else:
        formShell["unknown"] += 1
    offFExists = False
    for offF in formShell["offForms"]:
        if row[11] == offF["offForm"]:
            offFExists = True
            UpdateOffForm(row, offF)
            break
    if not offFExists:
        formShell["offForms"].append(AddNewOffForm(row))

def ParseDataToJson(data):
    formShells=[]
    for row in data:
        #TODO optimize
        for fs in formShells:
            if row[16] == fs["formShell"]:
                UpdateFormShell(row, fs)
                #add to obj
                break
        formShells.append(AddNewFormShell(row))
    return formShells
            
def DumpJsonToFile(jData, oFile):
    with open(oFile, 'w') as f:
        json.dump(jData, f, indent=4, sort_keys=True)

args = ParseArgs()
data = ReadCSVFile(args.filename)
headers = data.pop(0)
jData = ParseDataToJson(data)
DumpJsonToFile(jData, "/home/benjgause/FOOTBALL/auto-hit-charts/src/data/buchanan_output.json")
