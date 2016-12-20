#Profile/forms.py

from django import forms
from .models import Userdetail,Search

class PostForm(forms.ModelForm):

    class Meta:
        model = Userdetail
        fields = ('Fname','Lname','Year','Bio','Genre',
                  'Instruments','Address')
        
class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('Criteria',)
