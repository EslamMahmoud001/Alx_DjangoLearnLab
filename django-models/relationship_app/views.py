from django.shortcuts import render, redirect
from .models import Book
from django.views.generic import DetailView
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Create your views here.

def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html', "library", "from .models import Library"
    context_object_name = 'library'
    

# Function to check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'


# Admin View: Only accessible by users with 'Admin' role
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome to the Admin View!")


# Librarian View: Only accessible by users with 'Librarian' role
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian View!")


# Member View: Only accessible by users with 'Member' role
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome to the Member View!")
