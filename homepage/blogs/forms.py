from django.forms import ModelForm
from django import forms
from .models import Blogs,Register
from django.utils import timezone
from pagedown.widgets import PagedownWidget

class blogform(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget())
	class Meta:
		model = Blogs
		fields = ('name', 'topic', 'content','tags')

class registerform(ModelForm):
	class Meta:
		model = Register
		fields = ('firstname', 'lastname', 'email','username','password')

