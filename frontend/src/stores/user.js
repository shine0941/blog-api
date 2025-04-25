import { defineStore } from 'pinia'
// import axios from 'axios'
import api from '@/utils/api'

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    username: '',
  }),
  actions: {
    async login(username, password) {
      try {
        const res = await api.post('/token/', { username, password })
        this.token = res.data.access
        localStorage.setItem('token', this.token)

        // 取得用戶資訊
        const userRes = await api.get('/users/me/', {
          headers: { Authorization: `Bearer ${this.token}` },
        })
        this.username = userRes.data.username
      } catch (err) {
        throw new Error('登入失敗')
      }
    },
    logout() {
      this.token = ''
      this.username = ''
      localStorage.removeItem('token')
      alert('logout successed')
    },
  },
})