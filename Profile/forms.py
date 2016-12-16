#Profile/forms.py

from django import forms
from .models import Userdetail

class PostForm(forms.ModelForm):

    class Meta:
        model = Userdetail
        fields = ('Fname','Lname', 'Techlevel','Year','Rating','Bio','Instruments','Genre',)
        
class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('Criteria',)