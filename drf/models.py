from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    cast = models.CharField(max_length=50)
    release = models.CharField(max_length=10)

    def __str__(self):
        return self.title
