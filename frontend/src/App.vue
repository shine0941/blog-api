<template>
  <v-app>
    <AppToolBar />
    <v-container>
      <router-view />
    </v-container>
    <AppFooter />
  </v-app>
</template>

<script >
export default {
  name: 'App'
}
</script>
<script setup>
import AppToolBar from './components/AppToolBar.vue'
import AppFooter from './components/AppFooter.vue'
</script>

<!-- <template>
  <v-app>
    <v-main>
      <v-container>
        <v-icon size="36">mdi-home</v-icon>
      </v-container>
    </v-main>
  </v-app>
</template> -->
