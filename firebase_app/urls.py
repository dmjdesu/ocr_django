from django.urls import path

from . import views

urlpatterns = [
    path('', views.OCR.as_view(), name='index'),
]