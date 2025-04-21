# Blog API - Django REST Framework 專案

這是一個使用 Django + Django REST Framework 打造的部落格後端 API，支援使用者註冊、登入（JWT 驗證）、文章 CRUD 功能，適合作為後端工程師作品集練習與展示用。

## 📦 技術棧

- Python 3.10+
- Django 4.x
- Django REST Framework
- SimpleJWT（JWT 認證）
- PostgreSQL / SQLite（可切換）
- Redis（可選，作為快取）
- Render（部署）

## 🔧 安裝與執行

1. 克隆此專案

```bash
git clone https://github.com/shine0941/blog-api.git
cd blog-api

```

2. 建立虛擬環境

python3 -m venv env
source env/bin/activate

3. 安裝套件

pip install -r requirements.txt

4. 建立資料庫與啟動伺服器

python manage.py migrate
python manage.py runserver


伺服器將在 http://127.0.0.1:8000 運行。

---

## 🧪 測試 API

- 使用 Postman 或 curl 測試 API
- 預設路由可能包含：

  - `/api/token/`：取得 JWT
  - `/api/token/refresh/`：刷新 Token
  - `/api/articles/`：文章列表 / 建立 / 查詢 / 編輯 / 刪除
  - `/swagger/` 或 `/api/docs/`：Swagger API 文件（若啟用）

---

## 🚀 部署建議

- Render 或 Railway
- 可搭配 PostgreSQL 雲端資料庫
- .env 設定檔管理敏感資訊（SECRET_KEY、DEBUG、資料庫連線）

---

## 📁 專案結構

blog-api/
├── blog/               # 文章相關功能
├── users/              # 使用者註冊、登入
├── blog_project/           # 專案主設定
├── requirements.txt
├── manage.py
└── README.md


---

## 👤 作者資訊

- 作者：Yu Hsiang Chiu
- GitHub：https://github.com/shine0941
