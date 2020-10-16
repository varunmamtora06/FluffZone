from django import forms
from . import models


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = models.blog
        fields = ['title', 'img', 'body']

class CreateBreedForm(forms.ModelForm):
    class Meta:
        model = models.breed
        fields = ['img']

class CreateAdoptionForm(forms.ModelForm):
    
    class Meta:
        model = models.adoptPost
        fields = '__all__'
        exclude = ('owner',) #add comma to make it a tuple
