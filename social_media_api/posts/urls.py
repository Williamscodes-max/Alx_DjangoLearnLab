from django.urls import path
from .views import (
    PostListCreateView,
    PostDetailView,
    CommentCreateView,
    CommentDeleteView
)

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]