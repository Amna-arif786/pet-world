from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='care_home'),
    path('beginner/', views.beginner_guide, name='beginner_guide'),
    path('food/', views.food_guide, name='food_guide'),
    path('tips/<int:pk>/', views.tip_detail, name='tip_detail'),
    path('about/', views.about, name='care_about'),
    path('contact/', views.contact, name='care_contact'),
]
