#Profile/forms.py

from django import forms
from .models import Userdetail,Search

class PostForm(forms.ModelForm):

    class Meta:
        model = Userdetail
        fields = ('Username','Fname','Lname', 'Techlevel','Year','Rating','Bio','Genre',
                  'Address','Instruments',)
        
class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('Criteria',)