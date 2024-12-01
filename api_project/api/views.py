from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer
from .permissions import IsBookOwner

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Query the Book model
    serializer_class = BookSerializer  # Use the BookSerializer to format the data
    
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Queryset for retrieving, updating, and deleting books
    serializer_class = BookSerializer  # Serializer for formatting book data
    
    # Define permissions for different actions
    permission_classes = [IsAuthenticated, IsBookOwner]  # Apply custom permission here  # Only authenticated users can access the APId

    # You can also create more fine-grained permissions:
    def get_permissions(self):
        if self.action == 'create':  # Allow only admins to create books
            return [IsAdminUser()]
        return super().get_permissions()