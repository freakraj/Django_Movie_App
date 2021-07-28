from django.shortcuts import render
from django.views import View
from .models import Movie

# Class Based View
class MovieView(View):
    def get(self,request):
        action = Movie.objects.filter(category='act')
        drama = Movie.objects.filter(category='dra')
        comedy = Movie.objects.filter(category='com')
        romantic = Movie.objects.filter(category='rom')
        return render(request,'app/home.html', {'action':action,'drama':drama,'comedy':comedy,'romantic':romantic})

# Class Based View
class   MovieDetailiew(View):
    def get(self, request, pk):
        product = Movie.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product':product})







