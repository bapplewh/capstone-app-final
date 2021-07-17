from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('packages/', views.packages),
    path('clients/', views.clients),
]