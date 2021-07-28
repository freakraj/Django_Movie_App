# Self Creating urls for raj

from django.urls import path
from . import views 

urlpatterns = [
 
    path('search/', views.index, name="youtube-search")
]