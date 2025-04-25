<template>
    <v-toolbar>
      <v-toolbar-title>My Blog</v-toolbar-title>
      <v-spacer />
      <div v-if="user.token">
        👋 Hi, {{ user.username }}
        <v-btn @click="user.logout">登出</v-btn>
      </div>
      <div v-else>
        <v-btn @click="router.push('/login')">登入</v-btn>
      </div>
    </v-toolbar>
  </template>
  
  <script setup>
  import { useUserStore } from '@/stores/user'
  import { useRouter } from 'vue-router'
  
  const user = useUserStore()
  const router = useRouter()
  </script>
  