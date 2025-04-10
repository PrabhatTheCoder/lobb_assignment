# 🔗 Lobb Assignment - Scalable URL Shortener

A production-ready, distributed URL shortener built with **Django REST Framework**. It uses Snowflake ID generation and Base62 encoding for compact, globally unique short links.

---

## 🌐 Live Demo

**Frontend (Vercel deployed):**  
➡️ [https://lobb-assignment-ivory.vercel.app/](https://lobb-assignment-ivory.vercel.app/)

---

## 📌 Features

- 🔐 Unique short codes using Snowflake + Base62
- 🔁 Redirection to original URLs
- 📋 List all shortened URLs
- 📊 Track click counts (optional to extend)
- 🌍 Scalable & backend-agnostic design

---

## 🚀 API Endpoints

| Endpoint             | Method | Description                        |
|----------------------|--------|------------------------------------|
| `/shorten/`          | POST   | Shorten a long URL                 |
| `/<short_code>/`     | GET    | Redirect to the original URL       |
| `/list-urls/`        | GET    | List all shortened URLs            |

---

## 🔧 Setup & Run Locally

### 1. Clone the Repo
```bash
git clone <your-repo-url>
cd lobb_assignment
