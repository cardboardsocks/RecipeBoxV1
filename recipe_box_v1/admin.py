from django.contrib import admin

# Register your models here.
from recipe_box_v1.models import Author,Recipe
admin.site.register(Author)
admin.site.register(Recipe)
