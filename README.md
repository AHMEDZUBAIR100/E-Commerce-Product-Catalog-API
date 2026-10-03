# E-Commerce Product Catalog API

A lightweight, high-performance RESTful API for managing an e-commerce product catalog built using **FastAPI**, **SQLAlchemy**, and **Pydantic**.

---

## Features

- **CRUD Operations**: Complete functionality to Create, Read, Update, and Delete products.
- **Data Validation**: Built-in request/response validation using Pydantic models.
- **Database Integration**: SQLite database management using SQLAlchemy ORM (Declarative Mapping).
- **Interactive API Documentation**: Auto-generated Swagger UI and ReDoc endpoints.

---

## Tech Stack

* **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
* **Validation**: [Pydantic](https://docs.pydantic.dev/)
* **Database**: SQLite (default)
* **Server**: [Uvicorn](https://www.uvicorn.org/)

---

## Project Structure

```text
├── database.py         # Database configuration & session initialization
├── models.py           # SQLAlchemy database models
├── schemas.py          # Pydantic data schemas & validation rules
├── crud.py             # CRUD database logic
├── main.py             # FastAPI entry point
└── routers/
    └── products.py     # API routes for product endpoints
```

---

## Getting Started

### Prerequisites

* Python 3.10+
* `pip` package manager

### Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

4. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API Documentation**
   * **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   * **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints Summary

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| **POST** | `/products` | Create a new product | `201 Created` |
| **GET** | `/products` | Retrieve all products | `200 OK` |
| **PUT** | `/products/{product_id}` | Update product details | `200 OK` |
| **DELETE** | `/products/{product_id}` | Delete a product | `200 OK` |

---

## Data Models

### Product Schema Example (`POST` / `PUT`)

```json
{
  "name": "Wireless Mouse",
  "description": "Ergonomic 2.4GHz optical wireless mouse",
  "price": 29.99,
  "quantity": 150
}
```

### Validation Constraints

* `name`: String (1 to 100 characters)
* `description`: String (1 to 500 characters)
* `price`: Float (greater than 0)
* `quantity`: Integer (greater than or equal to 0)