<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col><h2>建立文章</h2></v-col>
        </v-row>
        <v-row>
          <v-col
            ><v-text-field v-model="form.title" label="標題"></v-text-field
          ></v-col>
        </v-row>
        <v-row>
          <v-col
            ><v-select
              v-model="form.category_id"
              label="分類"
              :items="categories"
              item-title="name"
              item-value="id"
            ></v-select
          ></v-col>
        </v-row>
        <v-row>
          <v-col
            ><v-combobox
              v-model="form.tag_ids"
              :items="tagOptions"
              label="標籤"
              multiple
            ></v-combobox
          ></v-col>
        </v-row>
        <v-row>
          <v-col
            ><v-textarea v-model="form.content" label="內容" outlined rows="6">
            </v-textarea
          ></v-col>
        </v-row>
        <v-row justify="end" class="mt-4">
          <v-col cols="auto">
            <v-btn color="primary" @click="submitArticle">儲存</v-btn>
          </v-col>
          <v-col cols="auto">
            <v-btn @click="cancel">取消</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>
<script>
import api from '@/utils/api'
export default {
  data() {
    return {
      form: {
        title: '',
        category_id: null,
        tag_ids: [],
        content: '',
      },
      categories: [{ id: 1, name: 'travel' }],
      tagOptions: [],
    }
  },
  methods: {
    async submitArticle() {
      console.log('送出資料：', this.form)
      this.token = localStorage.getItem('token') || ''
      try {
        const res = await api.post('/articles/', this.form, {
          headers: { Authorization: `Bearer ${this.token}` },
        })
        console.log('建立成功', res.data)
        this.$router.push('/') // 成功後導回首頁或文章列表
      } catch (err) {
        console.error('建立失敗', err)
      }
    },
    cancel() {
      // 導回上一頁或清空表單
      this.$router.back()
    },
  },
  mounted() {
    // 在這裡撈取分類與標籤
    // this.fetchCategories()
    // this.fetchTags()
  },
}
</script>
