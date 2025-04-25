<template>
  <v-app>
    
    <v-main>
      <v-container>
        <h2>文章列表</h2>        
        <ul>
          <li v-for="a in articles" :key="a.id">
            {{ a.title }}
          </li>
        </ul>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      articles: []
    }
  },
  async mounted() {
    const res = await fetch('/api/articles/')
    this.articles = await res.json()
  }
}
</script>