from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='breeds_home'),
    path('<int:pk>/', views.breed_detail, name='breed_detail'),
    path('about/', views.about, name='breeds_about'),
    path('contact/', views.contact, name='breeds_contact'),
]
