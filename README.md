# Rent_WebApp

# House Rent Website

This project is a **House Rent Website** similar to rent.com, built with **React** for the frontend and **Django** for the backend. It allows users to view house listings, post new rental properties, and manage their accounts securely. The project is structured into three main apps on the backend:

- **Home**: Fetches and displays house listings for the homepage.
- **Post**: Manages CRUD operations for rental property posts.
- **My Account**: Handles user registration, authentication, and profile management.

---

## Table of Contents
1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Installation](#installation)
4. [Backend Apps](#backend-apps)
5. [Frontend Setup](#frontend-setup)
6. [API Endpoints](#api-endpoints)
7. [Usage](#usage)
8. [Screenshots](#screenshots)
9. [License](#license)

---

## Features
- **User Authentication**: Secure registration and login using Django Token Authentication.
- **House Listings**: View all available houses with details like title, description, price, and location.
- **Post Management**: CRUD operations for house posts (Create, Read, Update, Delete).
- **Homepage Feed**: Displays the latest 5 house listings.
- **User Profiles**: Users can view their account details securely.

---

## Tech Stack
### **Frontend**:
<p align="left">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=react-router&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Axios-007FFF?style=for-the-badge&logo=axios&logoColor=white" />
</p>

### **Backend**:
<p align="left">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Django%20REST-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/CORS-000000?style=for-the-badge&logo=cors&logoColor=white" />
</p>

---

## Installation
Follow these steps to set up the project locally:

### **1. Clone the Repository**
```bash
https://github.com/your-username/house-rent-website.git
cd house-rent-website
```

### **2. Backend Setup**
```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django djangorestframework django-cors-headers

# Start Django project
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Create admin user
python manage.py runserver
```

The Django server will run at `http://localhost:8000/`

### **3. Frontend Setup**
```bash
cd frontend
npm install  # Install React dependencies
npm start    # Start React development server
```
The React server will run at `http://localhost:3000/`

---

## Backend Apps
### 1. **Home**
- Fetches and displays the latest house listings for the homepage.

### 2. **Post**
- Manages house listing operations:
    - **Create**: Add a new house.
    - **Read**: View all houses or individual house details.
    - **Update**: Edit house details.
    - **Delete**: Remove house posts.

### 3. **My Account**
- Handles user authentication, registration, and profile viewing.

---

## API Endpoints
| **Endpoint**            | **Method** | **Description**                      |
|-------------------------|------------|--------------------------------------|
| `/api/home/`            | GET        | Fetch homepage latest house listings |
| `/api/post/houses/`     | GET/POST   | View all houses / Create new house   |
| `/api/post/houses/{id}` | PUT/DELETE | Update or delete a specific house    |
| `/api/account/register/`| POST       | Register a new user                  |
| `/api/account/profile/` | GET        | View logged-in user profile          |

---

## Usage
1. **Register a User**:
   - Send a POST request to `/api/account/register/` with `username` and `password`.
2. **Login**:
   - Use the token authentication for secure requests.
3. **Post a House**:
   - Use `/api/post/houses/` to add a new house.
4. **View Houses**:
   - Fetch all available houses using the GET endpoint.
5. **Homepage**:
   - Visit `/api/home/` to see the latest posts.

---

## Screenshots
screenshots of the homepage, post page, and profile page here.

---

## License
This project is licensed under the MIT License.

---

### **Contact**
For inquiries or contributions:
- **Name**: Privertus Cosmas
- **Email**: priverdeprince@yahoo.com
- **GitHub**: [https://github.com/your-username](https://github.com/your-stark-priver)

---

> **Think Why, Then Execute Ideas**

