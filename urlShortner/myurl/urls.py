from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   path('urlShortener',urlshort,name='urlshort'),
   path('createUrl',createUrl,name="createUrl"),
   path('<str:uid>',goto,name="goto"),
   path('getlink/',fetchlink,name='getlink'),
]
