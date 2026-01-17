# from django.urls import path
# from .views import list_books, LibraryDetailView

# urlpatterns = [
#     path("books/", list_books, name="list_books"),
#     path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
# ]

# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
# from . import views

# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path(
#         'login/',
#         LoginView.as_view(template_name='relationship_app/login.html'),
#         name='login'
#     ),
#     path(
#         'logout/',
#         LogoutView.as_view(template_name='relationship_app/logout.html'),
#         name='logout'
#     ),
# ]

# from django.urls import path

# from .admin_view import admin_view
# from .librarian_view import librarian_view
# from .member_view import member_view

# urlpatterns = [
#     path('admin/', admin_view, name='admin_view'),
#     path('librarian/', librarian_view, name='librarian_view'),
#     path('member/', member_view, name='member_view'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('member/', views.member_view, name='member'),
# ]

from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('', include('relationship_app.urls')),
]
