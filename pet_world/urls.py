"""
URL configuration for pet_world project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pets import views as pets_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pets_views.home, name='home'),
    path('pets/', include('pets.pets_urls')),
    path('care/', include('care.care_urls')),
    path('breeds/', include('breeds.breeds_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
