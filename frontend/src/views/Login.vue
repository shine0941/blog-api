<template>
    <div>
      <h2>登入</h2>
      <form @submit.prevent="login">
        <input v-model="username" placeholder="使用者名稱" />
        <input v-model="password" type="password" placeholder="密碼" />
        <button>登入</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        error: ''
      }
    },
    methods: {
      async login() {
        try {
          const res = await fetch('/api/token/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: this.username, password: this.password })
          })
          if (!res.ok) throw new Error('登入失敗')
          const data = await res.json()
          localStorage.setItem('access', data.access)
          localStorage.setItem('refresh', data.refresh)
          this.$router.push('/')
        } catch (err) {
          this.error = err.message
        }
      }
    }
  }
  </script>