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

        # widgets = {
        #     'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Tommy'}),
        #     'breedName' : forms.TextInput(attrs={'class':'form-control','placeholder':'pitbull or cat'}),
        #     'health' : forms.TextInput(attrs={'class':'form-control','placeholder':'Good or ill'}),
        #     'gender' : forms.TextInput(attrs={'class':'form-control','placeholder':'male or female'}),
        #     'ageYears' : forms.TextInput(attrs={'class':'form-control','placeholder':'age in years'}),
        #     'location' : forms.TextInput(attrs={'class':'form-control','placeholder':'male or female'}),
        # }