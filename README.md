# 🔗 Lobb Assignment - Scalable URL Shortener

A **production-ready**, distributed URL shortener built with **Django REST Framework**. It generates compact, globally unique short links using **Snowflake ID generation** and **Base62 encoding**.

---

## 🌐 Live Demo

**Frontend (Vercel deployed):**  
➡️ [https://lobb-assignment.vercel.app/](https://lobb-assignment.vercel.app/)

---

## 📌 Features

- 🔐 Unique short codes using Snowflake + Base62
- 🔁 Instant redirection to original URLs
- 📋 List all previously shortened URLs
- 📊 Track click counts *(optional for future enhancement)*
- ⚙️ Backend-agnostic, scalable design

---

## 🚀 API Endpoints

| Endpoint             | Method | Description                        |
|----------------------|--------|------------------------------------|
| `/shorten/`          | POST   | Submit a long URL and receive a short one |
| `/<short_code>/`     | GET    | Redirects to the original long URL |
| `/list-urls/`        | GET    | Retrieves all shortened URLs       |

---

## 📦 Tech Stack

- **Backend:** Django, Django REST Framework
- **ID Generator:** Snowflake algorithm
- **Encoding:** Base62
- **Frontend:** [Deployed on Vercel](https://lobb-assignment.vercel.app/)
- **Database:** PostgreSQL (or compatible)

---

## 🛠️ Local Development

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd lobb_assignment
