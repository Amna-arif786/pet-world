from django.db import models


class FoodGuide(models.Model):
    PET_TYPES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('other', 'Other'),
    ]

    pet_type = models.CharField(max_length=20, choices=PET_TYPES, unique=True)
    title = models.CharField(max_length=120)
    daily_meals = models.CharField(max_length=100)
    good_foods = models.TextField()
    bad_foods = models.TextField()
    feeding_tips = models.TextField()
    water_tips = models.TextField(blank=True)

    def __str__(self):
        return self.title


class CareTip(models.Model):
    LEVELS = [
        ('beginner', 'Beginner'),
        ('daily', 'Daily Care'),
        ('health', 'Health'),
        ('home', 'Home Setup'),
    ]

    title = models.CharField(max_length=120)
    level = models.CharField(max_length=20, choices=LEVELS, default='beginner')
    pet_type = models.CharField(max_length=20, choices=FoodGuide.PET_TYPES, blank=True)
    summary = models.TextField()
    steps = models.TextField(help_text='Write each step on a new line')

    class Meta:
        ordering = ['level', 'title']

    def __str__(self):
        return self.title

    def step_list(self):
        return [s.strip() for s in self.steps.splitlines() if s.strip()]
