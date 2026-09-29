# Zomato-like Food Ordering & Sales Analytics Application

A full-stack food ordering application built using **Python Flask, MySQL, HTML, CSS, and JavaScript**.

The application allows users to select food items, add them to a cart, place orders, view previous orders, and analyze sales data through an analytics dashboard.

---

## Project Overview

This project combines a simple food ordering application with SQL-based sales analytics.

The application uses:

- **HTML, CSS, JavaScript** for the frontend
- **Python Flask** for the backend
- **MySQL** for data storage
- **SQL** for data analysis and reporting

The project also demonstrates how data entered through a web application can be stored in a relational database and later used for analytics.

---

## Features

### Food Ordering

- View available food items
- Add food items to cart
- Increase item quantity
- Calculate cart total
- Enter delivery address
- Place an order

### Order Management

- Store orders in MySQL
- View recent orders
- Display item, price, quantity, delivery address, and order date

### Sales Analytics Dashboard

The dashboard provides:

- Total revenue
- Revenue by item
- Revenue by category
- Revenue by payment method

### SQL Analytics

The project includes SQL queries for:

- Total revenue
- Revenue by item
- Revenue by category
- Revenue by payment method
- Total orders
- Orders by payment status
- Most ordered items
- Revenue by customer
- Orders and revenue by customer
- Customer order details
- Items ordered by category
- Revenue by date
- Items purchased in a specific order
- Customers with no orders

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| MySQL | Database |
| SQL | Data analysis |
| HTML | Web page structure |
| CSS | Web page styling |
| JavaScript | Frontend functionality |
| Git | Version control |
| GitHub | Source code management |

---

## Project Structure

```text
Zomato_Project
│
├── app.py
├── analytics.sql
├── .gitignore
├── README.md
│
├── templates
│   ├── index.html
│   ├── orders.html
│   └── analytics.html
│
└── static
    ├── style.css
    └── script.js