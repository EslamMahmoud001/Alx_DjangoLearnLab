from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.save()
        return redirect('book_list')
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'view_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('book_list')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # Redirects to login page upon successful registration
    template_name = "registration/signup.html"
    
