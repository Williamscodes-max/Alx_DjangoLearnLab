# LibraryProject


## Introduction
This project is a basic Django setup created to understand the Django development environment.

## Setup Instructions
1. Install Django using pip.
2. Run the development server:



Testing Strategy:
Unit tests were written using Django REST Framework’s APITestCase.
The tests cover CRUD operations for the Book API, including creating,
retrieving, updating, and deleting records. Custom serializer validation
for publication_year was also tested. All tests run using Django’s
isolated test database to ensure data integrity.

Running Tests:
python manage.py test api

