from django.shortcuts import render
from django.views.generic.base import TemplateView

# function based views


def home_view(request):
    return render(request, 'mybooks/home.html')


# class based views


class HomeView(TemplateView):
    template_name = "mybooks/home.html"
