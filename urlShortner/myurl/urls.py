from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   path('urlShortener',urlshort,name='urlshort'),
   path('createUrl',createUrl,name="createUrl")
]
