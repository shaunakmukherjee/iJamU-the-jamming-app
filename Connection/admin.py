#Connection/admin.py

from django.contrib import admin
from .models import Connection,Crequest

# Register your models here.
admin.site.register(Crequest)
admin.site.register(Connection)