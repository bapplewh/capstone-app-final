from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signup, name="signin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('packages/', views.packages, name="packages"),
    path('client/<str:pk_test>/', views.client, name="client"),
]