from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .models import Blogs,Register
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from django.utils.html import urlencode
from .forms import blogform,registerform
from django.utils import timezone
from django.utils.crypto import get_random_string
from taggit.managers import TaggableManager


# Create your views here.
def welcome(request):
	if request.session.get('username'):
		return render(request,'blogs/index.html',{'user':request.session['username'],'form':blogform()})
	return render(request,'blogs/welcome.html',{})

def page(request, blog_name):
	latest = Blogs.objects.all()[:5]
	tags=''
	category=''
	all_blogs = Blogs.objects.all()
	single_blog = Blogs.objects.get(topic=blog_name);
	return render(request,'blogs/single.html',{'single_blog':single_blog,'latest':latest,'tags':tags,'category':category,'blogs':all_blogs})

def taggedpage(request,tag):
	taggpost = Blogs.objects.filter(tags__name__in=[tag]);
	return render(request,'blogs/tagpost.html',{'blogs':taggpost,'tag':tag})

def index(request):
	if request.session.get('username'):
		return render(request,'blogs/index.html',{'form':blogform()})
	else:
		return redirect("/",{})	

def blogs(request):
		all_blogs = Blogs.objects.all().order_by('-pk');
		return render(request,'blogs/blogs.html',{'blogs':all_blogs})

def bloggers(request,name):
		all_blogs = Blogs.objects.filter(name=name);
		bloglist = Blogs.objects.all();
		return render(request,'blogs/bloggers.html',{'bloglist':bloglist,'blogs':all_blogs,'blogger':name})

def uploadblog(request):
	if request.method == 'POST':
		data = blogform(request.POST)
		if data.is_valid():
			new_data = data.save(commit=False)
			new_data.uploadtime = timezone.now()
			new_data.save()
			data.save_m2m()
			return render(request,'blogs/index.html',{'message':'Blog added Successfully','user':request.session['username'],'form':blogform()})	
		else:
			return render(request,'blogs/index.html',{'form':data,'message':'','user':data.is_valid(),'form':blogform()})	
	else:
		return render(request,'blogs/index.html',{'error_message':'please fill the blog'})

def register(request):
	if request.method == 'POST':
		data = registerform(request.POST)
		if data.is_valid():
			data.save()
			subject = 'Registration mail'
			message = 'Thank you for your registration and member of our company kritsnam technology '+ data.save(commit=False).username
			from_email = settings.EMAIL_HOST_USER
			to = [data.save(commit=False).email]
			send_mail(subject,message,from_email,to,fail_silently=True)

			return render(request,'blogs/welcome.html',{'success':'Registration mail is sent successfully on your registerd email id'})		
	else:
		return render(request,'blogs/welcome.html',{'error_message':'please fill the blog'})

def forgot(request):
	if request.method == 'POST':
		data = request.POST
		if data:
			token =get_random_string(length=32)
			request.session['token'] = token
			request.session['email'] = data['email']
			subject = 'Forgot password'
			message = 'Hi there, To create new password please click on the link given     http://127.0.0.1:8000/forgot/'+token
			from_email = settings.EMAIL_HOST_USER
			to = [data['email']]
			send_mail(subject,message,from_email,to,fail_silently=True)
			
			return render(request,'blogs/welcome.html',{'success':'Mail is sent successfully on your registerd email id'})		
	else:
		return render(request,'blogs/welcome.html',{'error_message':'please fill the blog'})

def forgotpage(request,tokenw):
		tokens = request.session.get('token')
		if tokens == tokenw:
			return render(request,'blogs/reset.html',{})
		else:
			return render(request,'blogs/reset.html',{})

def reset(request):
	if request.method =='POST':
		tokens = request.session.get('token')
		sessionemail = request.session.get('email')
		if tokens:
			user = Register.objects.filter(email= sessionemail)[0]
			user.password = request.POST['password']
			user.save()
			del request.session['token']
			return render(request,'blogs/welcome.html',{'success':'password is successfully changed'})				
		
		return render(request,'blogs/welcome.html',{'success':'Token is expired or link not exist'})				
	else:
		return render(request,'blogs/welcome.html',{'success':'Token is expired or link not exist'})				


def login_blog(request):
	if request.method == 'POST':
		data = request.POST
		form = Register.objects.filter(username= data['username'])
		if form:
			if form[0].password == data['password']:
				success = 'you are eligible to login'
				request.session['username'] = data['username']
				return render(request,'blogs/index.html',{'error':'','success':'','user':request.session['username'],'form':blogform()})
			return render(request,'blogs/welcome.html',{'error':'Wrong password try again','success':''})
		else:
			error = 'Wrong username and password'
			
			return render(request,'blogs/welcome.html',{'error':error,'success':''})
	else:
		return render(request,'blogs/welcome.html',{'error':''})	

def logout_blog(request):
	logout(request)
	return redirect("/",{})	

