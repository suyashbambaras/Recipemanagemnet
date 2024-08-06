from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipeid', 'name', 'ingredients', 'instructions', 'prep_time', 'cook_time', 'total_time', 'image', 'category')

admin.site.register(Recipe, RecipeAdmin)
