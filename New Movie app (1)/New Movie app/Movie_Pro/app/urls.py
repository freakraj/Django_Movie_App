from django.urls import path
from app import views
from django.conf import settings #this is import settings file
from django.conf.urls.static import static #this is import static file

urlpatterns = [
    path('', views.MovieView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.MovieDetailiew.as_view(), name='product-detail'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
