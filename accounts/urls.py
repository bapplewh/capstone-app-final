from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('testimonials/', views.testimonials, name="testimonials"),

    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logoutUser, name="logout"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('packages/', views.packages, name="packages"),
    path('client/<str:pk_test>/', views.client, name="client"),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('create_client/', views.createClient, name="create_client"),
    path('delete_client/<str:pk>/', views.deleteClient, name="delete_client"),
]