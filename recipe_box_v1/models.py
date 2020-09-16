from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title         = models.CharField(max_length =100)
    author        = models.ForeignKey(Author , on_delete=models.CASCADE)
    description   =  models.TextField()
    time_required = models.CharField(max_length = 15)
    instruction   =  models.TextField()

    def __str__(self):
        return self.title

class Favorites(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)