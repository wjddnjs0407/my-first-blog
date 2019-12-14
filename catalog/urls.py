from django.urls import path
from catalog import views

urlpatterns =[
    path("", views.PostlistView.as_view(), name="index"),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('food/', views.FoodlistView.as_view(), name='food'),
    path('ukfood/', views.UkfoodlistView.as_view(), name='ukfood'),
    path('francefood/', views.FrancefoodlistView.as_view(), name='francefood'),
    path('italyfood/', views.ItalyfoodlistView.as_view(), name='italyfood'),
    path('austfood/', views.AustfoodlistView.as_view(), name='austfood'),
    path('visit/', views.VisitlistView.as_view(), name='visit'),
    path('ukvisit/', views.UkvisitlistView.as_view(), name='ukvisit'),
    path('francevisit/', views.FrancevisitlistView.as_view(), name='francevisit'),
    path('italyvisit/', views.ItalyvisitlistView.as_view(), name='italyvisit'),
    path('austvisit/', views.AustvisitlistView.as_view(), name='austvisit'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),

]