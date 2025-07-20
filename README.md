# 🛍️ E-commerce API

A lightweight and scalable **E-commerce REST API** built with **FastAPI** and **MongoDB**, supporting product and order management with pagination.

🌐 **Live API**: [https://ecommerce-api-0woo.onrender.com](https://ecommerce-api-0woo.onrender.com)

---

## ⚙️ Tech Stack

- **Backend**: FastAPI
- **Database**: MongoDB (async via Motor)
- **Deployment**: Render
- **Utilities**: Pydantic, Uvicorn

---

## 📂 Project Structure
```
ecommerce-api/
│
├── main.py # FastAPI app entry point
├── database.py # MongoDB async connection setup
│
├── models/ # (Optional) Pydantic models (can be merged into schemas)
│
├── schemas/ # Request/Response models
│ ├── product.py
│ └── order.py
│
├── routes/ # API route definitions
│ ├── product.py
│ └── order.py
│
├── utils/
│ └── pagination.py # Utility for paginated response
│
├── requirements.txt # Python dependencies
└── .env (optional) # MongoDB credentials
```
---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ecommerce-api.git
cd ecommerce-api

```
## 2️⃣ Create virtual environment & install dependencies
```
python -m venv venv
source venv/bin/activate      # For macOS/Linux
# OR
venv\Scripts\activate         # For Windows

pip install -r requirements.txt
```
## 3️⃣ Add MongoDB URI
You can either:

Create a .env file with:
```
.env
MONGO_URL=mongodb+srv://<username>:<password>@<cluster-url>/<dbname>
```

## 4️⃣ Run the Server
```
bash
uvicorn main:app --reload
```
Server runs at: http://localhost:8000

---
## 📦 API Endpoints
📘 Products
➕ Create Product
```
bash
POST /products
```
Request Body:
```
json

{
  "name": "T-Shirt",
  "price": 499.99
}
```
📄 Get Products (Paginated)
```
pgsql
GET /products?limit=10&offset=0
```
Response:
```
json

{
  "data": [
    { "id": "...", "name": "T-Shirt", "price": 499.99 }
  ],
  "page": {
    "next": "10",
    "limit": 10,
    "previous": "-10"
  }
}
```
📦 Orders
➕ Create Order
```
bash
POST /orders
```
Request Body:
```
json
{
  "userId": "user123",
  "items": [
    { "productId": "abc123", "qty": 2 },
    { "productId": "def456", "qty": 1 }
  ]
}
```
📄 Get Orders for User
```
pgsql
GET /orders/{user_id}?limit=10&offset=0
```
Response:
```
json
{
  "data": [
    {
      "id": "...",
      "items": [
        {
          "productDetails": { "id": "...", "name": "T-Shirt" },
          "qty": 2
        }
      ],
      "total": 999.98
    }
  ],
  "page": {
    "next": "10",
    "limit": 10,
    "previous": "-10"
  }
}
```


☁️ Deployment
The API is deployed and live at:

🌐 https://ecommerce-api-0woo.onrender.com

You can view API documentation at:

📄 https://ecommerce-api-0woo.onrender.com/docs
