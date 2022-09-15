from django.contrib import admin
from django.urls import path

from .views import Home_page

urlspattern =[
    path('', Home_page),
    path('admin/', admin.site.urls),
]