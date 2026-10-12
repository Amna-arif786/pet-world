from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .context_processors import get_liked_pet_ids, set_liked_pet_ids
from .models import Pet


def home(request):
    pets = Pet.objects.all()[:6]
    top_liked = Pet.objects.order_by('-likes')[:3]
    return render(request, 'pets/home.html', {
        'pets': pets,
        'top_liked': top_liked,
        'total_pets': Pet.objects.count(),
        'photo_count': Pet.objects.exclude(photo='').exclude(photo=None).count(),
    })


def about(request):
    return render(request, 'pets/about.html')


def contact(request):
    message_sent = False
    if request.method == 'POST':
        message_sent = True
    return render(request, 'pets/contact.html', {'message_sent': message_sent})


def pet_list(request):
    category = request.GET.get('category', '')
    pets = Pet.objects.all()
    if category:
        pets = pets.filter(category=category)
    return render(request, 'pets/pet_list.html', {
        'pets': pets,
        'selected_category': category,
    })


def gallery(request):
    pets = Pet.objects.exclude(photo='').exclude(photo=None)
    return render(request, 'pets/gallery.html', {'pets': pets})


def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pets/pet_detail.html', {
        'pet': pet,
        'is_liked': pet.pk in get_liked_pet_ids(request),
    })


def like_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    liked = False
    if request.method == 'POST':
        liked_ids = get_liked_pet_ids(request)
        if pet.pk in liked_ids:
            liked_ids.remove(pet.pk)
            Pet.objects.filter(pk=pet.pk, likes__gt=0).update(likes=F('likes') - 1)
            liked = False
        else:
            liked_ids.add(pet.pk)
            Pet.objects.filter(pk=pet.pk).update(likes=F('likes') + 1)
            liked = True
        set_liked_pet_ids(request, liked_ids)
        pet.refresh_from_db(fields=['likes'])
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'ok': True, 'likes': pet.likes, 'liked': liked})
    next_url = request.POST.get('next') or request.GET.get('next')
    if next_url:
        return redirect(next_url)
    return redirect('pet_detail', pk=pet.pk)


def add_pet(request):
    error = ''
    if request.method == 'POST':
        name = request.POST.get('name', '').strip() or 'Unnamed'
        photo = request.FILES.get('photo')
        if not photo:
            error = 'Please upload a pet photo to share.'
        else:
            Pet.objects.create(
                name=name,
                owner_name=request.POST.get('owner_name', '').strip() or 'Anonymous',
                category=request.POST.get('category', 'other'),
                age=int(request.POST.get('age') or 1),
                description=request.POST.get('description', ''),
                photo=photo,
            )
            return redirect('gallery')
    return render(request, 'pets/add_pet.html', {'error': error})
