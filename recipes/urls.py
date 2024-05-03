from django.urls import path
from . import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"), #Home
    path('recipes/<slug:id>/', views.recipe, name="recipe"), #Página das notícias individuais
    
]