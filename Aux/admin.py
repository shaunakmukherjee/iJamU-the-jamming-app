from django.contrib import admin
from .models import Post
from .models import Userdetails
from .models import Search


admin.site.register(Post)
admin.site.register(Userdetails)
admin.site.register(Search)

# Register your models here.
