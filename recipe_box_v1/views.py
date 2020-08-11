from django.shortcuts import render,HttpResponseRedirect,reverse
from recipe_box_v1.models import Recipe, Author
from recipe_box_v1.forms import AddAuthorForm,AddRecipeForm
# Create your views here.
def index(request):
    return render(request,'index.html',{'all_recipes':Recipe.objects.all()})

def recipe_detail(request,recipe_id):
    _recipe_detail = Recipe.objects.filter(id=recipe_id).first()
    context = {
        "recipe_detail":_recipe_detail
    }
    return render(request,'recipe_detail.html',context)

def author_detail(request,author_id):
    _author_detail =Recipe.objects.filter(author__id= author_id)
    _author_name =Author.objects.get(id= author_id)
  
    
    context = {
        "author_detail":_author_detail,
        "author_name":_author_name
    }
    return render(request,'author_detail.html',context)


def add_new_author_form_view(request):
    
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name = data.get('name'),
                bio = data.get('bio'),
  
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddAuthorForm()
    return render(request,"addauthor.html",{'form':form})

def add_new_recipe_form_view(request):
    
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data.get('title'),
                author = data.get('author'),
                description = data.get('description'),
                time_required = data.get('time_required'),
                instruction = data.get('instruction')
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddRecipeForm()
    return render(request,"addrecipe.html",{'form':form})