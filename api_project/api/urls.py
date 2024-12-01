from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Define the route for the BookList view
    
    # Include the router's URLs for all CRUD operations
    path('', include(router.urls)),  # Includes all routes for BookViewSet
    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token retrieval
]