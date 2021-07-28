from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','description','category','movie_image','language','production_date','Timestamp']

