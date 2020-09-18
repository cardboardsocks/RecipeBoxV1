from django.contrib import admin
from recipe_box_v1.models import Author,Recipe, Favorites


admin.site.register(Author)
admin.site.register(Recipe)
admin.site.register(Favorites)