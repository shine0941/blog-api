<template>
  <v-app>
    <v-main>
      <v-container>
        <h2>文章列表</h2>
        <v-row justify="end">
          <v-col cols="auto">
            <v-btn color="primary" @click="router.push('/createarticle')"
              >建立文章</v-btn
            >
          </v-col>
        </v-row>
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
import api from '@/utils/api'
export default {
  data() {
    return {
      articles: [],
    }
  },
  async mounted() {
    const res = await api.get('/articles/')
    this.articles = await res['data']
  },
}
</script>
<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
</script>
