# from django.urls import path
# from .views import simple_message, HomeView

# urlpatterns = [
#     path("", HomeView.as_view(), name="home"),
#     path("hello/", simple_message, name="hello"),
# ]

# from django.urls import path
# from .views import HomeView, simple_message, SignUpView

# urlpatterns = [
#     path("", HomeView.as_view(), name="home"),
#     path("hello/", simple_message, name="hello"),
#     path("signup/", SignUpView.as_view(), name="signup"),
# ]

from django.urls import path
from django.views.generic import TemplateView
from . import views

# urlpatterns = [
#     path("", TemplateView.as_view(template_name="bookshelf/home.html"), name="home"),
# ]


urlpatterns = [
    path('books/', views.books_list, name='book_list'),
    path('books/add/', views.create_book, name='create_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]

