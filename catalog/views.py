from django.shortcuts import render
from catalog.models import Post, Country, Genre
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView

# Create your views here.

class PostlistView(generic.ListView):
    model = Post
    template_name = "catalog/post_list.html"
    context_object_name = "posts"

class PostDetailView(generic.DetailView):
    model = Post

class FoodlistView(generic.ListView):
    model = Post
    template_name = "catalog/food.html"
    queryset = Post.objects.filter(genre__id=1)
    context_object_name = "foods"

class VisitlistView(generic.ListView):
    model = Post
    template_name = "catalog/visit.html"
    queryset = Post.objects.filter(genre__id=2)
    context_object_name = "visits"


class UkfoodlistView(generic.ListView):
    model = Post
    template_name = "catalog/ukfood.html"
    queryset = Post.objects.filter(genre__id=1, country__id=1)
    context_object_name = "ukfoods"

class UkvisitlistView(generic.ListView):
    model = Post
    template_name = "catalog/ukvisit.html"
    queryset = Post.objects.filter(genre__id=2, country__id=1)
    context_object_name = "ukvisits"

class FrancefoodlistView(generic.ListView):
    model = Post
    template_name = "catalog/francefood.html"
    queryset = Post.objects.filter(genre__id=1, country__id=2)
    context_object_name = "francefoods"

class FrancevisitlistView(generic.ListView):
    model = Post
    template_name = "catalog/francevisit.html"
    queryset = Post.objects.filter(genre__id=2, country__id=2)
    context_object_name = "francevisits"

class ItalyfoodlistView(generic.ListView):
    model = Post
    template_name = "catalog/italyfood.html"
    queryset = Post.objects.filter(genre__id=1, country__id__in=[3,4,5])
    context_object_name = "italyfoods"

class ItalyvisitlistView(generic.ListView):
    model = Post
    template_name = "catalog/italyvisit.html"
    queryset = Post.objects.filter(genre__id=2, country__id__in=[3,4,5])
    context_object_name = "italyvisits"

class AustfoodlistView(generic.ListView):
    model = Post
    template_name = "catalog/austfood.html"
    queryset = Post.objects.filter(genre__id=1, country__id=6)
    context_object_name = "austfoods"

class AustvisitlistView(generic.ListView):
    model = Post
    template_name = "catalog/austvisit.html"
    queryset = Post.objects.filter(genre__id=2, country__id=6)
    context_object_name = "austvisits"

class PostCreate(CreateView):
    model = Post
    fields = '__all__'

class PostUpdate(UpdateView):
    model = Post
    fields = ['title','author','country','genre','data']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('index')


