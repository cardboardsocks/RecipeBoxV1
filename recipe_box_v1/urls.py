
from django.urls import path
from recipe_box_v1 import views
urlpatterns = [
    path('',views.index),
    path('recipe/<int:recipe_id>/',views.recipe_detail),
    path('author/<int:author_id>/',views.author_detail),

    
]
