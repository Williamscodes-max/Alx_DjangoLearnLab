# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
# from .views import BookViewSet  # <-- must match exactly
# from .views import BookList

# router = DefaultRouter()
# router.register(r'books', BookViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('token/', obtain_auth_token, name='api_token_auth'),
#     path('books/', BookList.as_view(), name='book-list'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Old ListAPIView endpoint (ALX wants this kept)
    path('books/', BookList.as_view(), name='book-list'),

    # Router endpoints (CRUD)
    path('', include(router.urls)),
]
