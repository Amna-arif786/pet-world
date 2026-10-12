from django.shortcuts import render, get_object_or_404
from .models import Breed


def home(request):
    pet_type = request.GET.get('type', '')
    breeds = Breed.objects.all()
    if pet_type:
        breeds = breeds.filter(pet_type=pet_type)
    return render(request, 'breeds/home.html', {
        'breeds': breeds,
        'selected_type': pet_type,
        'beginner_count': Breed.objects.filter(good_for_beginners=True).count(),
    })


def breed_detail(request, pk):
    breed = get_object_or_404(Breed, pk=pk)
    related = Breed.objects.filter(pet_type=breed.pet_type).exclude(pk=pk)[:3]
    return render(request, 'breeds/detail.html', {
        'breed': breed,
        'related': related,
    })


def about(request):
    return render(request, 'breeds/about.html')


def contact(request):
    return render(request, 'breeds/contact.html')
