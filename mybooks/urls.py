from django.urls import path
from . import views

urlpatterns = [
    # function based views
    path('', views.home_view, name='home'),
    # class based views
    path('class/', views.HomeView.as_view(), name='class_home'),
]
