from django.shortcuts import render, get_object_or_404
from .models import FoodGuide, CareTip
from breeds.models import Breed


def home(request):
    tips = CareTip.objects.all()[:8]
    return render(request, 'care/home.html', {
        'tips': tips,
        'food_guides': FoodGuide.objects.all(),
    })


def beginner_guide(request):
    return render(request, 'care/beginner.html', {
        'tips': CareTip.objects.filter(level='beginner'),
        'food_guides': FoodGuide.objects.all(),
        'easy_breeds': Breed.objects.filter(good_for_beginners=True)[:6],
    })


def food_guide(request):
    pet_type = request.GET.get('type', '')
    guides = FoodGuide.objects.all()
    selected = None
    if pet_type:
        selected = FoodGuide.objects.filter(pet_type=pet_type).first()
    return render(request, 'care/food.html', {
        'guides': guides,
        'selected': selected,
        'selected_type': pet_type,
    })


def tip_detail(request, pk):
    tip = get_object_or_404(CareTip, pk=pk)
    return render(request, 'care/tip_detail.html', {'tip': tip})


def about(request):
    return render(request, 'care/about.html')


def contact(request):
    return render(request, 'care/contact.html')
