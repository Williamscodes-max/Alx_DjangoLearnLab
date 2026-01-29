# Permissions and Groups Setup

## Groups
- **Admins** → Full access (view, create, edit, delete books)
- **Editors** → Can view, create, and edit books
- **Viewers** → Can only view books

## Permissions
- Defined in `Book` model: can_view, can_create, can_edit, can_delete
- Assigned to groups via Django Admin

## Views
- Protected using `@permission_required` decorators in `views.py`
- Users without permission will see a 403 Forbidden page

## Testing
- Assign users to groups in admin
- Log in as each user and test the access according to their group

## SSL
SSL certs should be installed on production.



# Security Measures Implemented:

# 1. SECURE_SSL_REDIRECT: All HTTP requests redirect to HTTPS
# 2. HSTS: Browsers are instructed to only access the site via HTTPS for 1 year
# 3. Secure Cookies: SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE ensure cookies are only sent over HTTPS
# 4. X_FRAME_OPTIONS: Deny framing to protect against clickjacking
# 5. SECURE_CONTENT_TYPE_NOSNIFF: Prevents MIME type sniffing
# 6. SECURE_BROWSER_XSS_FILTER: Enables browser XSS filter to reduce XSS attacks

