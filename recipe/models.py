from django.db import models

# Create your models here.

from django.db import models

class Recipe(models.Model):
    recipeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField(help_text="Preparation time in minutes")
    cook_time = models.IntegerField(help_text="Cooking time in minutes")
    total_time = models.IntegerField(help_text="Total time in minutes", blank=True, null=True)
    image =models.ImageField(upload_to='images')
    CATEGORY_CHOICES = [
        ('Veg', 'Vegetarian'),
        ('NonVeg', 'Non-Vegetarian'),
    ]
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='Veg')


    def __str__(self):
        return self.name
