from django.contrib import admin
from django.urls import path
from django.views import *

urlpatterns = [
    path('', home.as_view(), name='home'),
]