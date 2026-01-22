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

urlpatterns = [
    path("", TemplateView.as_view(template_name="bookshelf/home.html"), name="home"),
]


