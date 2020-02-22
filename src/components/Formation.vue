<template>
  <div>
    <svg id="formation"/>
  </div>
</template>

<script>
  /* eslint-disable */
  import _ from "lodash";
  import * as d3 from "d3";
  export default {
    data() {
      return {
        formation: "Ace",
        height: 0,
        width: 0,
        margin: { top: 0, right: 0, bottom: 0, left: 0 },
      }
    },
    mounted () {
      this.setDimensions();
      this.initChart();
    },
    methods: {
      setDimensions() {
        if (this.width !== this.$el.offsetWidth) {
          this.width = this.$el.offsetWidth
          this.height = 80
        }
      },
      initChart() {
        let height = this.height - this.margin.top - this.margin.bottom;
        let width = this.width - this.margin.left - this.margin.right;
        let svg = d3
          .select("#formation")
          .attr("width", width)
          .attr("height", height)

        const g = svg.append("g").attr("class", "main_group");

        // draw core offensive linemen
        let oline = [
          {
            pos: "rb",
            xplace: 5,
            yplace: 0
          },
          {
            pos: "qb",
            xplace: 5,
            yplace: 2
          },
          {
            pos: "wr",
            xplace: 0,
            yplace: 2
          },
          {
            pos: "wr",
            xplace: 10,
            yplace: 2
          },
          {
            pos: "te",
            xplace: 2,
            yplace: 3
          },
          {
            pos: "tackle",
            xplace: 3,
            yplace: 3
          },
          {
            pos: "guard",
            xplace: 4,
            yplace: 3
          },
          {
            pos: "center",
            xplace: 5,
            yplace: 3
          },
          {
            pos: "guard",
            xplace: 6,
            yplace: 3
          },
          {
            pos: "tackle",
            xplace: 7,
            yplace: 3
          },
          {
            pos: "te",
            xplace: 8,
            yplace: 3
          },
        ]
        let marginLeftRight = width / 5
        let xScale = d3.scaleBand()
          .domain(d3.range(0, 11, 1))
          .range([marginLeftRight, width - marginLeftRight])
          .padding([0.3]);
        
        let yScale = d3.scaleBand()
          .domain([3,2,1,0])
          .range([height - 10, 5])
        let players = g.selectAll('.players')
          .data(oline)
          .join('rect')
            .attr('x', d => xScale(d.xplace))
            .attr('y', d => yScale(d.yplace))
            .attr('width', xScale.bandwidth())
            .attr('height', 10)
            .attr('stroke', 'black')
            .attr('fill', d => {
              if (d.pos !== 'center') {
                return 'white'
              }
              return 'black'
            })
            .attr('rx', d => {
              if (d.pos !== 'center') {
                return 5
              }
              return 0
            })
      }
    },
  }
</script>

<style>

</style>