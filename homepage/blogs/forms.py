from django.forms import ModelForm
from .models import Blogs,Register
from django.utils import timezone


class blogform(ModelForm):
	class Meta:
		model = Blogs
		fields = ('name', 'topic', 'content')

class registerform(ModelForm):
	class Meta:
		model = Register
		fields = ('firstname', 'lastname', 'email','username','password')
