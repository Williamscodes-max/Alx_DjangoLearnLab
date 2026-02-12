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


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.post_list, name='home'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     # path('login/', views.user_login, name='login'),    # your login view
#     # path('logout/', views.user_logout, name='logout'), # your logout view
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('', views.post_list, name='post_list'),
# ]


from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)




urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]



