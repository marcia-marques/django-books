from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from .forms import BookForm


# function based views


def home_view(request):
    return render(request, 'mybooks/home.html')


def book_list(request):
    return render(request, 'mybooks/book_list.html')


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
    template_name = "mybooks/home.html"
