from django.db import models


class Breed(models.Model):
    PET_TYPES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=120)
    pet_type = models.CharField(max_length=20, choices=PET_TYPES, default='dog')
    temperament = models.CharField(max_length=200)
    size = models.CharField(max_length=50, help_text='Small / Medium / Large')
    lifespan = models.CharField(max_length=50, blank=True)
    good_for_beginners = models.BooleanField(default=True)
    overview = models.TextField()
    daily_care = models.TextField(help_text='How to deal with this pet daily')
    food_guide = models.TextField(help_text='What to feed and how often')
    avoid_food = models.TextField(help_text='Foods that are dangerous')
    common_mistakes = models.TextField(blank=True)
    fun_fact = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['pet_type', 'name']

    def __str__(self):
        return f'{self.name} ({self.get_pet_type_display()})'
