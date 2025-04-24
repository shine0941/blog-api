<template>
  <div>
    <h2>文章列表</h2>
    <div>login</div>
    <v-btn icon>
      <v-icon>mdi-account</v-icon>
    </v-btn>
    <v-icon>mdi-home</v-icon>

    <ul>
      <li v-for="a in articles" :key="a.id">
        {{ a.title }}
      </li>
    </ul>
  </div>
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