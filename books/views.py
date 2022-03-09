from django.shortcuts import render
from .models import Book

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html",
                {"books": books})
    
    
    
    
    
    
    
    
# def add_contact(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
