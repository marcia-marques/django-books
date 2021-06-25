from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # function based views
    path('', views.home_view, name='home'),
    # class based views
    path('class/', views.HomeView.as_view(), name='class_home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
