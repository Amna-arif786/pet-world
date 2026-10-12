from django.db import models


class Pet(models.Model):
    CATEGORY_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100, blank=True, default='Anonymous')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='dog')
    age = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='pets/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
