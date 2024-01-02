# My Unsplash Backend API

A robust Django REST API for managing photo collections, featuring user authentication and photo management capabilities.

## 🌟 Features

- **User Authentication**
  - Token-based authentication
  - User registration and login
  - Password verification
  
- **Photo Management**
  - Create, read, update, and delete photo entries
  - User-specific photo collections
  - Secure access control
  
- **API Documentation**
  - Swagger UI integration
  - ReDoc support

## 🛠 Tech Stack

- Django 3.2.19
- Django REST Framework 3.14.0
- PostgreSQL Database
- Token Authentication
- Swagger/OpenAPI Documentation

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL
- pip

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd unsplash-backend
```

2. Create and activate virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file in the root directory with:
```
DATABASE_URL=your_postgresql_url
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

## 📚 API Documentation

Access the API documentation at:
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## 🔑 Authentication Endpoints

### Register New User
```
POST /signup
```
Request body:
```json
{
    "username": "user",
    "password": "password",
    "email": "user@example.com"
}
```

### Login
```
POST /login
```
Request body:
```json
{
    "username": "user",
    "password": "password"
}
```

## 📸 Photo Management Endpoints

### Get User Photos
```
GET /photos/
```
*Requires authentication token*

### Add New Photo
```
POST /photos/
```
Request body:
```json
{
    "name": "Photo Name",
    "link": "https://example.com/photo.jpg",
    "description": "Photo description"
}
```
*Requires authentication token*

## 🔒 Security

- Token-based authentication
- User-specific data isolation
- Password hashing
- Permission-based access control

## 🚀 Deployment

The project is configured for deployment on Vercel with the following features:
- Python 3.9 runtime
- Automatic builds and deployments
- PostgreSQL database support

## 📝 License

This project is licensed under the MIT License 

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ✨ Acknowledgments

- Built with Django REST Framework
- Inspired by Unsplash
- Uses drf-yasg for API documentation
