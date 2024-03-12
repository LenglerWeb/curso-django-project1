from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), #Home
    path('recipes/<slug:id>/', views.recipe), #Página das notícias individuais
    
]