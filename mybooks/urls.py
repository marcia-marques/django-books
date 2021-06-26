from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # function based views
    path('', views.home_view, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.book_upload, name='book_upload'),
    path('books/update/<int:pk>/', views.book_update, name='book_update'),
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'),
    # class based views
    path('class/', views.HomeView.as_view(), name='class_home'),
    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', views.BookUploadView.as_view(), name='class_book_upload'),
    path('class/books/<int:pk>/', views.BookUpdateView.as_view(), name='class_book_update'),
    path('class/books/<int:pk>/', views.BookDeleteView.as_view(), name='class_book_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
