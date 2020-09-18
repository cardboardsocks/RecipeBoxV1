from django.shortcuts import render,HttpResponseRedirect,reverse, redirect
from recipe_box_v1.models import Recipe, Author, Favorites
from recipe_box_v1.forms import AddAuthorForm,AddRecipeForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
# Create your views here.

def index(request):
    all_recipes = Recipe.objects.all()
    all_authors = Author.objects.all()
    total_recipes = all_recipes.count()
    total_author = all_authors.count()
    
    context = {'all_recipes':all_recipes,'total_recipes':total_recipes,'total_author':total_author}
    return render(request,'index.html',context)

@login_required
def edit_recipe_view(request, recipe_id):
    edit_recipe = Recipe.objects.get(id=recipe_id)
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            edit_recipe.title = data["title"]
            edit_recipe.description = data["description"]
            edit_recipe.time_required = data["time_required"]
            edit_recipe.instructions = data["instruction"]
            edit_recipe.save()
        return HttpResponseRedirect(reverse("recipe", args=[edit_recipe.id]))
    data = {
        "title": edit_recipe.title,
        "description": edit_recipe.description,
        "time_required": edit_recipe.time_required,
        "instruction": edit_recipe.instructions,
    }
    form = AddRecipeForm(initial=data)
    return render(request, "generic_form.html", {"form": form})

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

def author_favorite(request, author_id):
    author = Author.objects.get(id=author_id)
    favorite = Favorites.objects.filter(author=author)
    return render(request, "favorites.html", {"favorite": favorite, "author": author.name})


    
@staff_member_required(login_url='login_page')
def add_new_author_form_view(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                u_name = data.get('name')
                u_pass = data.get('password')
                signup_user = User.objects.create_user(username = u_name,password=u_pass)

                Author.objects.create(
                    name = data.get('name'),
                    bio = data.get('bio'),
                    user= signup_user
    
                )
                return HttpResponseRedirect(reverse("homepage"))
        form = AddAuthorForm()
        return render(request,"addauthor.html",{'form':form})
    else:
         messages.info(request,"Permission Denied !!! you are not staff memeber")
         return redirect('/')

@login_required(login_url='login_page')
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

@login_required
def favorite_recipe(request, recipe_id):
    if Favorites.objects.filter(author=Author.objects.get(user=request.user), recipe=Recipe.objects.get(id=recipe_id)):
        return HttpResponseRedirect(reverse("recipe", args=[recipe_id]))
    else:
        Favorites.objects.create(
        author=Author.objects.get(user=request.user),
        recipe=Recipe.objects.get(id=recipe_id),
    )
    return HttpResponseRedirect(reverse("recipe", args=[recipe_id]))
    if not request.user.is_staff:
        form.fields['author'] = forms.ModelChoiceField(queryset=Author.objects.filter(name=request.user))
    return render(request,"addrecipe.html",{'form':form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    else:
        if request.method == "POST":
                    u_name = request.POST.get('username')
                    u_password =request.POST.get('password')
                    user = authenticate(request,username=u_name,password=u_password)
                    if user is not None:
                        login(request,user)
                        return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
                    else:
                        messages.info(request,"username or password is incorrect")
        
        return render (request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login')
