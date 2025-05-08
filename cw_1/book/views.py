from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book/book_detail.html', {'book': book})
