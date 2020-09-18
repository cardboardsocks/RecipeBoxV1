from django.urls import path
from recipe_box_v1 import views
urlpatterns = [    
    path("", views.index, name="homepage"),
    path("author/<int:author_id>/", views.author_detail),
    path("addauthor/", views.add_new_author_form_view, name="addauthor"),
    path("author/<int:author_id>/favorites/", views.author_favorite),
    path("recipe/<int:recipe_id>/", views.recipe_detail, name="recipe"),
    path("addrecipe/", views.add_new_recipe_form_view, name="addrecipe"),
    path("recipe/<int:recipe_id>/edit/", views.edit_recipe_view),
    path("recipe/<int:recipe_id>/favorites/", views.favorite_recipe),
    path("login/", views.login_view, name="login_page"),
    path("logout/", views.logout_view, name="logout_page"),
]
