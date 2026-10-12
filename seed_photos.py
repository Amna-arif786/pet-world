"""Attach sample photos to existing pets (downloads once)."""
import os
import urllib.request
from pathlib import Path

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pet_world.settings')
django.setup()

from django.core.files import File
from pets.models import Pet

MEDIA_PETS = Path('media/pets')
MEDIA_PETS.mkdir(parents=True, exist_ok=True)

SAMPLES = [
    ('Buddy', 'https://images.unsplash.com/photo-1552053831-71594a27632d?w=800&q=80', 'buddy.jpg', 'Sara', 12),
    ('Milo', 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&q=80', 'milo.jpg', 'Ahmed', 8),
    ('Kiwi', 'https://images.unsplash.com/photo-1552728089-57bdde30beb3?w=800&q=80', 'kiwi.jpg', 'Noor', 5),
    ('Luna', 'https://images.unsplash.com/photo-1574158622682-e40e69881006?w=800&q=80', 'luna.jpg', 'Amna', 15),
    ('Max', 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=800&q=80', 'max.jpg', 'Ali', 9),
]

for name, url, filename, owner, likes in SAMPLES:
    pet = Pet.objects.filter(name=name).first()
    if not pet:
        continue
    pet.owner_name = owner
    pet.likes = likes
    dest = MEDIA_PETS / filename
    if not dest.exists():
        try:
            urllib.request.urlretrieve(url, dest)
            print('Downloaded', filename)
        except Exception as exc:
            print('Skip download', filename, exc)
            continue
    if not pet.photo:
        with open(dest, 'rb') as f:
            pet.photo.save(filename, File(f), save=False)
    pet.save()
    print('Updated', pet.name)

print('Done. Pets with photos:', Pet.objects.exclude(photo='').exclude(photo=None).count())
