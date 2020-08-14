
from django.urls import path
from recipe_box_v1 import views
urlpatterns = [
    path('login/',views.login_view,name="login_page"),                   
    path('logout/', views.logout_view,name="logout_page"),                 
                  
    path('',views.index,name="homepage"),
    path('recipe/<int:recipe_id>/',views.recipe_detail),
    path('author/<int:author_id>/',views.author_detail),
    path('addauthor/',views.add_new_author_form_view),
    path('addrecipe/',views.add_new_recipe_form_view),

    
]
