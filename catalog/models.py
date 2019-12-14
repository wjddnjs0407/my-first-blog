from django.db import models
import uuid
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    objects = models.Manager()
    name = models.CharField(
        max_length = 200,
        help_text = "게시글의 장르를 입력하세요.(예 : 맛집)")

    def __str__(self):
        return self.name

class Country(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    country = models.ForeignKey("Country",on_delete=models.SET_NULL,null=True)
    genre = models.ManyToManyField(Genre)
    data = models.TextField(
        max_length = 1000000,
        help_text=""
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

    