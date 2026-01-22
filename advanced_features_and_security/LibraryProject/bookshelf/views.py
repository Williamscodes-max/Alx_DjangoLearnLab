# from django.http import HttpResponse
# from django.views.generic import TemplateView
# from django.shortcuts import render


# def simple_message(request):
#     return HttpResponse("Hello, this is a function-based view.")


# class HomeView(TemplateView):
#     template_name = "bookshelf/home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["message"] = "Welcome to Django Templates & Static Files"
#         return context

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

 

class HomeView(TemplateView):
    template_name = "home.html"
   
