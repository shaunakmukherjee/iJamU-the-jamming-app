from django import forms

from .models import Userdetails, Search

class PostForm(forms.ModelForm):

    class Meta:
        model = Userdetails
        fields = ('Username', 'Fname','Lname', 'Techlevel','Rating','Bio','Instruments','Genre',)


class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('Instruments','Genre',)