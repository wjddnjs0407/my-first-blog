from django.contrib import admin
from .models import Genre
from .models import Country
from .models import Post

# Register your models here.
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Post)