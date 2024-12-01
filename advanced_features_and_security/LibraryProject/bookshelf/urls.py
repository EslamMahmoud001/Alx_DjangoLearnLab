from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.create_book, name='create_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('view/<int:book_id>/', views.view_book, name='view_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path("api/books", views.BookListCreateAPIView.as_view(), name="book_list_create"),
]