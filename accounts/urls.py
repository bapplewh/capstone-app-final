from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('testimonials/', views.testimonials),
    path('signup/', views.signup),
    path('dashboard/', views.dashboard),
    path('packages/', views.packages),
    path('client/<str:pk_test>/', views.client),
]