<template>
  <div class="min-h-screen p-8 flex items-center justify-center">
    <div class="bg-white w-1/5 border rounded-md">
      <div class="flex flex-row-reverse">
        <div class="text-right px-2 border text-xl">8x</div>
      </div>
      <div class="flex items-stretch px-4 py-2 text-xs">
        <!-- replace with table -->
        <div class="flex-1 text-left">
          <div class="font-semibold underline">
            Routes
          </div>
          <div>
            Slant-Arrow 1x
            <br/>
            Zone 5x
          </div>
        </div>
        <div class="flex-1 text-right">
          <div class="font-semibold underline">
            Actions
          </div>
          <div>
            QK 1x
            <br/>
            ST 4x
            <br/>
            WK 1x
          </div>
        </div>
      </div>
      <div>
        <Formation/>
      </div>
      <div class="flex items-stretch px-1 py-1 text-xs">
        <div class="flex-1"></div>
        <div class="flex-1 text-center">
          <div class="font-semibold underline">
            Power
          </div>
          1
        </div>
        <div class="flex-1 text-center">
          <div class="font-semibold underline">
            Stretch
          </div>
          1
        </div>
        <div class="flex-1"></div>
      </div>
      <div class="flex items-stretch px-1 py-1">
        <div class="flex-1"></div>
        <div class="flex-1 text-center border">Ace</div>
        <div class="flex-1 text-right text-xs pt-2">75% pass</div>
      </div>
    </div>
  </div>
</template>

<script>
import Formation from './Formation.vue'
export default {
  name: 'Dashboard',
  components: {
    Formation
  }
};
</script>