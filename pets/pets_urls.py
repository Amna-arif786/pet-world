from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pets_home'),
    path('about/', views.about, name='pets_about'),
    path('contact/', views.contact, name='pets_contact'),
    path('list/', views.pet_list, name='pet_list'),
    path('gallery/', views.gallery, name='gallery'),
    path('add/', views.add_pet, name='add_pet'),
    path('<int:pk>/', views.pet_detail, name='pet_detail'),
    path('<int:pk>/like/', views.like_pet, name='like_pet'),
]
