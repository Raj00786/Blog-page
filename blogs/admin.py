from django.contrib import admin

# Register your models here.
from .models import Blogs,Users

admin.site.register(Blogs)
admin.site.register(Users)
