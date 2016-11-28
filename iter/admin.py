from django.contrib import admin
from .models import Userdetails
from .models import Search
from .models import Connections

admin.site.register(Userdetails)
admin.site.register(Search)
admin.site.register(Connections)
# Register your models here.
