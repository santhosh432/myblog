from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    ''' business logic '''
    return render(request, template_name='blog/home.html')

def new_home(request):
    return HttpResponse('This is my new home....')

def home_contact(request):
    return render(request, template_name='blog/contact.html')

def home_blog(request):
    return render(request, template_name='blog/blog.html')