# Token-Based Authentication Setup

## **Overview**
This API uses Django REST Framework's token-based authentication to secure endpoints. Users can log in with their credentials to receive a token and use it to access protected endpoints.

---

## **Endpoints**

1. **Login Endpoint**
   - Path: `/api/accounts/login/`
   - Method: `POST`
   - Description: Authenticates a user and returns their token.

   **Request**:
   ```json
   {
     "username": "testuser",
     "password": "securepassword123"
   }
