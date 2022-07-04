from django.shortcuts import render
from books.models import Book
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm

# Create your views here.
def book_overview(request):
    books = Book.objects.all().order_by('-publication_date')
    context = {
        'books': books
    }
    return render(request, 'book_overview.html', context)

def book_detail(request, pk):
    book = Book.objects.get(pk= pk)
    context = {
        'book': book
    }
    return render(request,'book_detail.html', context)

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    # success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'