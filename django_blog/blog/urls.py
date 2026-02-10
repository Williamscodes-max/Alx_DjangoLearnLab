# from django.urls import path
# from . import views
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('', views.post_list, name='home'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('tag/<str:tag>/', views.post_list, name='posts_by_tag'),  # optional if you filter by tags
#     path('login/', views.user_login, name='login'),  # make sure you have login view
#     path('logout/', views.user_logout, name='logout'),  # logout view
#     path('register/', views.user_register, name='register'),  # registration view
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls')),  # 👈 CONNECT BLOG
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
