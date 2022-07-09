from multiprocessing import context
from django.shortcuts import render
from .models import Book
from books.models import Book
from .forms import BorrowForm


# Create your views here.
def book_overview(request):
    books = Book.objects.all().order_by('-publication_date')
    context = {
        'books': books
    }
    return render(request, 'book_temps/book_overview.html', context)

def book_detail(request, pk):
    book = Book.objects.get(pk= pk)
    context = {
        'book': book
    }
    return render(request,'book_temps/book_detail.html', context)

def borrow(request):
    form = BorrowForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'book_temps/borrow.html',context)
    

