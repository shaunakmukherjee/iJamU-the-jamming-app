#Connection/admin.py

from django.contrib import admin
from .models import Connection,Crequest, Endorsement, Endorsedetails

# Register your models here.
admin.site.register(Crequest)
admin.site.register(Connection)
admin.site.register(Endorsement)
admin.site.register(Endorsedetails)
