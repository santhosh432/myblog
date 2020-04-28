from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegisteration, PostForm, PostModelForm
from .models import Post
# from .forms import PostForm
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

def create_post(request):

    if request.method == 'POST':
        post_form = PostModelForm(request.POST)
        # print(post_form.title)
        print(request.POST.get('title'))
        if post_form.is_valid():

            post_form.save()

            return redirect('all_posts')

    else:
        post_form = PostModelForm()

    context = {'post_form':post_form}
    return render(request, template_name='blog/create_post.html', context=context)


def edit_post(request, pk=None):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post_form = PostModelForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('all_posts')
    else:
        post_form = PostModelForm(instance=post)
    context = {'post_form': post_form}

    return render(request, template_name='blog/create_post.html', context=context)

def post_delete(request, pk=None):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('all_posts')


