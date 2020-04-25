from django.shortcuts import render, HttpResponse
from .forms import UserRegisteration
from .models import Post
# Create your views here.

def home(request):
    ''' business logic '''

    # context = {'my_form': UserRegisteration()}
    return render(request, template_name='blog/home.html')

def new_home(request):

    return HttpResponse('This is my new home....')

def home_contact(request):
    return render(request, template_name='blog/contact.html')

def home_blog(request):
    return render(request, template_name='blog/blog.html')

def home_about_me(request):
    return render(request, template_name='blog/about_me.html')

def all_posts(request):
    post = Post.objects.all()
    context = {'my_post' : post}
    return render(request, template_name='blog/all_post.html', context=context)