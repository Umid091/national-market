# national-market
🛒 Django Marketplace Platform

A full-featured Marketplace web application built with Django, following a modular monolithic architecture.
This project was developed by a 3-member backend-focused team as a portfolio-level production-style system.

📌 Project Overview

This platform allows:

Sellers to create and manage products

Buyers to browse, search, and purchase products

Users to manage cart and wishlist

Order tracking and review system

Role-based access control

Architecture: Monolithic, app-based Django structure

👥 Team
Role	Name	Responsibilities
Team Lead	Sanjar	Users app, Orders app, Role-based access
Backend Developer	Umid	Products app, Reviews app
Backend Developer	Lutfullo	Cart app, Wishlist app
🏗 Tech Stack

Backend

Python 3.x

Django

PostgreSQL (Production)

SQLite (Development)

Frontend

HTML5

CSS3

Vanilla JavaScript

Django Template Language

Security

Role-based permissions

CSRF protection

LoginRequired decorators

Environment-based settings

DEBUG=False in production

📦 Project Structure
marketplace/
│
├── users/
├── products/
├── cart/
├── wishlist/
├── orders/
├── reviews/
│
├── templates/
├── static/
└── manage.py
🔐 Users App

Custom User model based on AbstractUser.

Features

Registration (Buyer / Seller role selection)

Login / Logout

Profile management

Role-based access control

Only sellers can create products

🛍 Products App
Models

Category

Product

Features

Full Product CRUD

Image upload

Search (by title)

Filter (category, price range)

Sorting

Pagination (10 items per page)

Seller-only edit/delete access

🛒 Cart App
Features

Add to cart

Remove from cart

Update quantity

Automatic total calculation

Stock validation (cannot exceed available stock)

❤️ Wishlist App
Features

Add/remove products

Prevent duplicate entries

Linked to authenticated users

📦 Orders App
Models

Order

OrderItem

Features

Checkout process

Stock reduction after order

Order history

Order status tracking:

Pending

Confirmed

Shipped

Delivered

Cancelled

Sellers can update status for their products

⭐ Reviews App
Features

One review per user per product

Rating (1–5)

Automatic average rating calculation

Comment system

🎨 Frontend Features

Base layout (base.html)

Global navbar & footer

Responsive design

Product cards

Seller dashboard

Order history page

Checkout page

Cart & Wishlist UI

⚙️ Installation
git clone https://github.com/your-username/marketplace.git
cd marketplace

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
🌍 Environment Variables

Create a .env file:

SECRET_KEY=your_secret_key
DEBUG=False
DATABASE_URL=your_database_url
🚀 Deployment

Recommended:

PostgreSQL

Gunicorn

Nginx (for VPS)

Render / Railway / VPS deployment

✅ Project Completion Criteria

All CRUD operations fully functional

Role-based access correctly enforced

Order workflow complete

Clean modular structure

No critical bugs

Organized Git commit history

📈 Future Improvements

REST API (Django REST Framework)

JWT Authentication

Payment Gateway Integration

Docker support

Email Notifications

Admin analytics dashboard

📜 License

This project was built for educational and portfolio purposes.
