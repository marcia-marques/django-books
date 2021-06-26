from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm


# function based views


def home_view(request):
    return render(request, 'mybooks/home.html')


def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'mybooks/book_list.html', context)


def book_upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'mybooks/book_upload.html', {'form': form})


# class based views


class HomeView(TemplateView):
    template_name = 'mybooks/home.html'


class BookListView(ListView):
    model = Book
    template_name = 'mybooks/book_list.html'
    context_object_name = 'books'


class BookUploadView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'mybooks/book_upload.html'
