from django.shortcuts import render,redirect
from .models import Blogs,Users
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from django.utils.html import urlencode
from .forms import blogform


# Create your views here.
def welcome(request):
	if request.session.get('username'):
		return render(request,'blogs/index.html',{})
	return render(request,'blogs/welcome.html',{})

def page(request, blog_name):
	# blog_name = blog_name.split('/')
	# return HttpResponse(blog_name)
	single_blog = Blogs.objects.get(topic=blog_name);
	return render(request,'blogs/single.html',{'single_blog':single_blog})

def index(request):
	if request.session.get('username'):
		return render(request,'blogs/index.html',{})
	else:
		return redirect("/",{})	

def blogs(request):
		all_blogs = Blogs.objects.all();
		return render(request,'blogs/blogs.html',{'blogs':all_blogs})

def uploadblog(request):
	if request.method == 'POST':
		data = blogform(request.POST)
		# blog = Blogs()
		# blog.name = data['name']
		# blog.topic = data['topic']
		# if data['profile']=='':
		# 	blog.profile ='https://cdn4.iconfinder.com/data/icons/rcons-user/32/boss_man-512.png'
		# blog.content = data['content']
		# blog.save()
		if data.is_valid():
			data.save()
		
		# return redirect("/blogs")
		return render(request,'blogs/index.html',{'message':'Blog is added successfully'})		
	else:
		return render(request,'blogs/index.html',{'error_message':'please fill the blog'})

def login_blog(request):
	if request.method == 'POST':
		data = request.POST
		error='' 
		success=''
		is_user = authenticate(username=data['username'],password=data['password'])
		if is_user:
			request.session['username'] = data['username']
			success ='Logged in Successfully....You will be redirected....'
			return redirect("/index.html")
		else:
			error = 'username or password is incorrect please try again or register'
		
			return render(request,'blogs/welcome.html',{'error':error,'success':success})	
	else:
		return render(request,'blogs/welcome.html',{'error':data})	

def logout_blog(request):
	logout(request)
	return redirect("/",{})	
