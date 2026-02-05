# Advanced API Project with Django REST Framework

## Project Overview
This project is a RESTful API built with Django and Django REST Framework (DRF) to manage **Authors** and **Books**.  
It supports CRUD operations for books, nested serialization for authors, filtering, searching, ordering, and token-based authentication.

- **Models**: Author, Book  
- **Features**:
  - Create, Read, Update, Delete (CRUD) operations for books
  - Nested serialization: Authors include their books
  - Filtering by author, title, and publication year
  - Searching by title or author name
  - Ordering by title or publication year
  - Token-based authentication for protected endpoints

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-github-repo-url>
cd advanced-api-project
