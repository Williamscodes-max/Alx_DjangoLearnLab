# Django Blog Project

This is a simple blog application built with Django as part of the ALX Django Learn Lab.

## Features
- Create and view blog posts
- View post details
- Add comments to posts
- Admin panel for managing content

## Technologies Used
- Python
- Django
- SQLite

## How to Run
1. Clone the repository
2. Navigate to the project directory
3. Run migrations:
   python manage.py migrate
4. Start the server:
   python manage.py runserver
5. Open browser at:
   http://127.0.0.1:8000/



## User Authentication System

This project implements a full user authentication system for the Django blog application.

### Features Implemented
- User registration
- User login
- User logout
- User profile management

### Authentication Flow

#### Registration
Users can create an account using the `/register/` URL.  
The registration form is based on Django’s `UserCreationForm` with an added email field.

#### Login
Users can log in at `/login/` using Django’s built-in authentication system.

#### Logout
Authenticated users can log out via `/logout/`.

#### Profile Management
Logged-in users can view and update their profile information at `/profile/`.  
This page is protected using Django’s `login_required` decorator.

### URLs Configuration
Authentication URLs are defined in `blog/urls.py`:
- `/register/`
- `/login/`
- `/logout/`
- `/profile/`

### Templates
Authentication templates are located in:

templates/
├── registration/
│ └── login.html
├── blog/
│ ├── register.html
│ └── profile.html



### Security
- CSRF protection is enabled on all forms
- Passwords are securely hashed using Django’s authentication system
- Restricted pages require authentication

### How to Test
1. Run the server:
2. Register a new user at `/register/`
3. Log in at `/login/`
4. Access `/profile/`
5. Log out at `/logout/`



## Blog Post Management Features

The blog supports full CRUD operations for posts.

### Features
- List all posts
- View single post
- Create posts (authenticated users)
- Edit and delete posts (authors only)

### Permissions
- Only logged-in users can create posts
- Only post authors can edit or delete posts

### URLs
- /posts/
- /posts/new/
- /posts/<id>/
- /posts/<id>/edit/
- /posts/<id>/delete/
