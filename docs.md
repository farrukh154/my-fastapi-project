
---

# API Documentation

This document provides an overview of the API endpoints and their usage. For more detailed, interactive documentation, visit the Swagger UI.

## Base URL

All endpoints are available at:
```
http://localhost:8000
```

## Endpoints

### 1. User Registration

- **URL**: `/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response** (Success):
  ```json
  {
    "id": 1,
    "username": "your_username"
  }
  ```
- **Error Response** (Username already exists):
  ```json
  {
    "detail": "Username already registered"
  }
  ```

### 2. User Login

- **URL**: `/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response** (Success):
  ```json
  {
    "message": "Login successful"
  }
  ```
- **Error Response** (Invalid credentials):
  ```json
  {
    "detail": "Invalid credentials"
  }
  ```

### 3. Create Post

- **URL**: `/posts/`
- **Method**: `POST`
- **Request Parameters**:
  - `user_id` (int): The ID of the user creating the post.
- **Request Body**:
  ```json
  {
    "title": "Post title",
    "content": "Post content"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "title": "Post title",
    "content": "Post content",
    "user_id": 1
  }
  ```

### 4. Get User Posts

- **URL**: `/users/{user_id}/posts`
- **Method**: `GET`
- **Response** (Success):
  ```json
  [
    {
      "id": 1,
      "title": "Post title",
      "content": "Post content"
    }
  ]
  ```

## Swagger UI

For an interactive view of the API, test requests, and auto-generated documentation, visit:

(http://localhost:8000/docs)

---

