from django.forms import ModelForm
from .models import Blogs

class blogform(ModelForm):
	class Meta:
		model = Blogs
		fields = ('name', 'topic', 'content','profile')
