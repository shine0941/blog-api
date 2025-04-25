<template>
  <v-container>
    <v-form @submit.prevent="submit">
      <v-text-field v-model="username" label="帳號" />
      <v-text-field v-model="password" label="密碼" type="password" />
      <v-btn type="submit" color="primary">登入</v-btn>
    </v-form>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const user = useUserStore()

const username = ref('')
const password = ref('')

async function submit() {
  try {
    await user.login(username.value, password.value)
    router.push('/')
  } catch (err) {
    alert('登入失敗')
  }
}
</script>
