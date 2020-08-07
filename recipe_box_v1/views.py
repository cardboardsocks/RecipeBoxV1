from django.shortcuts import render
from recipe_box_v1.models import Recipe, Author
# Create your views here.
def index(request):
    return render(request,'index.html',{'all_recipes':Recipe.objects.all()})

def recipe_detail(request,recipe_id):
    _recipe_detail = Recipe.objects.filter(id=recipe_id )
    context = {
        "recipe_detail":_recipe_detail
    }
    return render(request,'recipe_detail.html',context)

def author_detail(request,author_id):
    author_detail =Recipe.objects.filter(id=author_id)
    context = {
        "author_detail":author_detail
    }
    return render(request,'author_detail.html',context)