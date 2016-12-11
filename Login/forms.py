from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import Search,Userdetail



class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('Criteria',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Userdetail
        fields = ('Username', 'Fname','Lname', 'Techlevel','Year','Rating','Bio','Instruments','Genre',)