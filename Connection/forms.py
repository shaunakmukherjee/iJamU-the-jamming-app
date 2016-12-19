#Connection/forms.py

from django import forms
from .models import Userdetail,Endorsedetails,Search
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Userdetail
        fields = ('Fname','Lname', 'Techlevel','Nickname','Year','Rating','Bio','Genre',
                  'Address','Instruments',)

class EndorseForm(forms.ModelForm):

    class Meta:
        model = Endorsedetails
        fields = ('Techlevel','Rating','Comments')

        
class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('Criteria',)
