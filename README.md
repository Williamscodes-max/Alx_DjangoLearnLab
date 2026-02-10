# Advanced API Project – Testing Documentation

## Overview
This project uses Django Rest Framework (DRF) to build and test API endpoints
for managing Authors and Books. Unit tests are written to ensure correctness
of CRUD operations, filtering, searching, ordering, authentication, and
permissions.

---

## Testing Framework
- Django built-in test framework (`django.test.TestCase`)
- Django REST Framework test utilities (`APIClient`)
- Tests are located in: `api/test_views.py`

---

## Separate Test Database
Django automatically creates a **separate test database** when running tests.
This ensures that production and development data are never affected.

When the following command is executed:

```bash
python manage.py test api
