from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.OCR.as_view(), name='index'),
    url(r'^show/(?P<id>\d+)/$', views.show, name='show'),
]