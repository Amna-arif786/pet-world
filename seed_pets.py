import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pet_world.settings')
django.setup()

from pets.models import Pet

if Pet.objects.count() == 0:
    Pet.objects.bulk_create([
        Pet(name='Buddy', category='dog', age=3, description='Friendly golden dog who loves walks.'),
        Pet(name='Milo', category='cat', age=2, description='Calm indoor cat with soft fur.'),
        Pet(name='Kiwi', category='bird', age=1, description='Colorful bird that chirps all day.'),
        Pet(name='Luna', category='cat', age=4, description='Playful cat who loves yarn balls.'),
        Pet(name='Max', category='dog', age=5, description='Loyal companion and great with kids.'),
    ])
    print('Sample pets added')
else:
    print('Pets already exist:', Pet.objects.count())
