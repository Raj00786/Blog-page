from django.contrib import admin

# Register your models here.
from .models import Blogs,Register

admin.site.register(Blogs)
admin.site.register(Register)
