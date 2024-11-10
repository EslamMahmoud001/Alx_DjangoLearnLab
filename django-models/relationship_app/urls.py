from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Map the URL to the function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV to show library details
]