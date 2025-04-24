// import { defineConfig } from 'vite'
// import vue from '@vitejs/plugin-vue'
// import path from 'path'

// export default defineConfig({
//   plugins: [vue()],
//   build: {
//     outDir: '../blog_project/static', // 將靜態檔打包進 Django 的 static 資料夾
//     emptyOutDir: true,
//   },
//   resolve: {
//     alias: {
//       '@': path.resolve(__dirname, './src'),
//     },
//   },
//   server: {
//     proxy: {
//       '/api': 'http://localhost:8000',
//     },
//   }
  
// })

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from 'vite-plugin-vuetify'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vuetify({
      autoImport: true, // 這個打開才會自動註冊 <v-icon>、<v-btn> 等組件
    }),
  ],
})
