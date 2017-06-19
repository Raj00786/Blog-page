from django.shortcuts import render,redirect
from .models import Blogs,Register
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from django.utils.html import urlencode
from .forms import blogform,registerform
from django.utils import timezone


# Create your views here.
def welcome(request):
	if request.session.get('username'):
		return render(request,'blogs/index.html',{'user':request.session['username']})
	return render(request,'blogs/welcome.html',{})

def page(request, blog_name):
	latest = Blogs.objects.all()[:5]
	tags=''
	category=''
	single_blog = Blogs.objects.get(topic=blog_name);
	return render(request,'blogs/single.html',{'single_blog':single_blog,'latest':latest,'tags':tags,'category':category})

def index(request):
	if request.session.get('username'):
		return render(request,'blogs/index.html')
	else:
		return redirect("/",{})	

def blogs(request):
		all_blogs = Blogs.objects.all();
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
			return render(request,'blogs/index.html',{'message':'Blog added Successfully','user':request.session['username']})	
		else:
			return render(request,'blogs/index.html',{'form':data,'message':'','user':data.is_valid()})	
	else:
		return render(request,'blogs/index.html',{'error_message':'please fill the blog'})

def register(request):
	if request.method == 'POST':
		data = registerform(request.POST)
		if data.is_valid():
			data.save()
		return render(request,'blogs/welcome.html',{'success':'User is added successfully'})		
	else:
		return render(request,'blogs/welcome.html',{'error_message':'please fill the blog'})


def login_blog(request):
	if request.method == 'POST':
		data = request.POST
		form = Register.objects.filter(username= data['username'])
		if form:
			if form[0].password == data['password']:
				success = 'you are eligible to login'
				request.session['username'] = data['username']
				return render(request,'blogs/index.html',{'error':'','success':'','user':request.session['username']})
			return render(request,'blogs/welcome.html',{'error':'Wrong password try again','success':''})
		else:
			error = 'Wrong username and password'
			return render(request,'blogs/welcome.html',{'error':error,'success':''})
	else:
		return render(request,'blogs/welcome.html',{'error':data})	

def logout_blog(request):
	logout(request)
	return redirect("/",{})	

