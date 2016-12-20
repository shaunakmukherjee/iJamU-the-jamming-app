#Profile/admin.py

from django.contrib import admin
from .models import Userdetail,Search

# Register your models here.
admin.site.register(Userdetail)
admin.site.register(Search)