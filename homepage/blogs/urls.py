from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.welcome,name='welcome'),

    url(r'^index',views.index,name='index'),
    url(r'^blogs/$',views.blogs,name='blogs'),

    url(r'^blogs/(?P<blog_name>.+)/$', views.page),

    url(r'^add',views.uploadblog,name='uploadblog'),
    url(r'^login',views.login_blog,name='login_blog'),
    url(r'^logout',views.logout_blog,name='logout_blog'),
]
