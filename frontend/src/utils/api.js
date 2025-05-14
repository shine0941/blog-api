// src/utils/api.js
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8001/api/', // 根據你的 API 路徑調整
  withCredentials: true, // 如果你有使用 cookies 或 JWT 放在 httpOnly cookie
})

export default api
