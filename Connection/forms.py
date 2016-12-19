#Connection/forms.py

from django import forms
from .models import Endorsedetails
from django.contrib.auth.models import User


class EndorseForm(forms.ModelForm):

    class Meta:
        model = Endorsedetails
        fields = ('Username','Nickname','Techlevel','Rating','Comments')
