# Inventory Management System - Group 11

## Group Members
- Melissa Happy Cephas - 166705
- Nimo Abdille Jama - 171538
- Were Shawn - 151633
- Wayne Gichuki - 166607
- Brian Kamau - 85052


## Project Description
This project is an **Inventory Management System** built with Django and Django REST Framework (DRF).  
It allows managing Categories, Suppliers, Products, Customers, and Orders through a secure REST API.


## Models

### 1. Category
- Fields: `name`, `description`
- Description: Represents product categories (e.g., Electronics, Furniture).

### 2. Supplier
- Fields: `name`, `contact_email`, `phone_number`
- Description: Represents suppliers who provide products.

### 3. Product
- Fields: `category`, `supplier`, `name`, `description`, `quantity`, `price`
- Description: Represents items in inventory linked to a category and supplier.
- Validation: Quantity cannot be negative.

### 4. Customer
- Fields: `name`, `email`, `phone_number`
- Description: Represents customers placing orders.

### 5. Order
- Fields: `customer`, `product`, `quantity`, `order_date`
- Description: Represents orders made by customers.
- Validation: Quantity must be greater than 0.

---

## Serializers
- Convert models to JSON for API communication.
- Include validation rules:
  - Product quantity cannot be negative.
  - Order quantity must be greater than zero.

---

## Views / ViewSets
- Each model has a **ModelViewSet** for CRUD operations.
- Permissions:
  - Anyone can **GET** (read).
  - Only authenticated users can **POST, PUT, DELETE**.
- Authentication: JWT (JSON Web Token)

---

## API URLs

| Model      | Method | URL                                | Description                 |
|------------|--------|------------------------------------|-----------------------------|
| Category   | GET    | /api/categories/                   | List all categories         |
| Category   | POST   | /api/categories/                   | Create a new category       |
| Category   | PUT    | /api/categories/{id}/              | Update a category           |
| Category   | DELETE | /api/categories/{id}/              | Delete a category           |
| Supplier   | GET    | /api/suppliers/                    | List all suppliers          |
| Supplier   | POST   | /api/suppliers/                    | Create a new supplier       |
| Supplier   | PUT    | /api/suppliers/{id}/               | Update a supplier           |
| Supplier   | DELETE | /api/suppliers/{id}/               | Delete a supplier           |
| Product    | GET    | /api/products/                     | List all products           |
| Product    | POST   | /api/products/                     | Create a new product        |
| Product    | PUT    | /api/products/{id}/                | Update a product            |
| Product    | DELETE | /api/products/{id}/                | Delete a product            |
| Customer   | GET    | /api/customers/                     | List all customers          |
| Customer   | POST   | /api/customers/                     | Create a new customer       |
| Customer   | PUT    | /api/customers/{id}/                | Update a customer           |
| Customer   | DELETE | /api/customers/{id}/                | Delete a customer           |
| Order      | GET    | /api/orders/                        | List all orders             |
| Order      | POST   | /api/orders/                        | Create a new order          |
| Order      | PUT    | /api/orders/{id}/                   | Update an order             |
| Order      | DELETE | /api/orders/{id}/                   | Delete an order             |
| Auth       | POST   | /api/token/                         | Get JWT token               |
| Auth       | POST   | /api/token/refresh/                 | Refresh JWT token           |

---

## Testing

All API endpoints were tested using **Postman** with JWT authentication:

- **Categories**: tested GET, POST, PUT, DELETE  
- **Suppliers**: tested GET, POST, PUT, DELETE  
- **Products**: tested GET, POST, PUT, DELETE  
- **Customers**: tested GET, POST, PUT, DELETE  
- **Orders**: tested GET, POST, PUT, DELETE  

## Testing

All API endpoint test screenshots are saved in the `screenshots/` folder in this repository.
