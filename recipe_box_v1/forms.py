from django import forms
from recipe_box_v1.models import Author, Recipe

class AddAuthorForm(forms.Form):    
      
    name = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Write the name of author. . .'
        }
    ))
    bio = forms.CharField(widget= forms.Textarea(
           attrs={
            'class':'form-control',
            'placeholder':'Write the bio of author. . .'
        }
    ))
  
    
class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=30,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Write the title of recipe. . .'
        }
    ))
    author = forms.ModelChoiceField(queryset=Author.objects.all(),
    widget=forms.Select(attrs={'class':'dropdown-item'}))
    description = forms.CharField(widget=forms.Textarea(
           attrs={
            'class':'form-control',
            'placeholder':'add description. . .'
        }
    ))
    time_required = forms.CharField(max_length = 15,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'time required i.e one hour. . .'
        }
    ))
    instruction = forms.CharField(widget=forms.Textarea(
           attrs={
            'class':'form-control',
            'placeholder':'add instructions. . .'
        }
    ))