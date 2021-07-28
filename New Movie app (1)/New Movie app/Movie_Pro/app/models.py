from django.db import models

# Create your models here.
CATEGORY_CHOICES =(
    ('act','Action'),
    ('dra','Drama'),
    ('com','Comedy'),
    ('rom','Romance'),
)

LANGUAGE_CHOICES =(
    ('English','English'),
    ('Hindi','Hindi'),
)


class  Movie(models.Model):
    title = models.CharField(max_length=100) 
    description = models.TextField()
    movie_image = models.ImageField(upload_to='productimg')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=4)
    language = models.CharField(choices=LANGUAGE_CHOICES,max_length=8)
    production_date = models.DateField()
    Timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)
  