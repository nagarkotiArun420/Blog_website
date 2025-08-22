from django.shortcuts import get_object_or_404, redirect, render
from blog_category.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from . forms import BlogForm, CategoryForm, AddUserForm, EditUserForm, EditPostForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



# Create your views here.

@login_required(login_url='login')

def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()
    
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_categories(request):
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_categories.html', context)

def edit_categories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method=="POST":
        form = CategoryForm(request.POST,instance = category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category,
    }
    return render(request,"dashboard/edit_categories.html",context)

def delete_categories(request,pk):
    category = get_object_or_404(Category,pk = pk)
    category.delete()
    return render(request,'dashboard/categories.html')

def posts(request):
    posts = Blogs.objects.all()
    context={
        'posts':posts,
    }
    return render(request,'dashboard/posts.html',context)

def add_post(request):
    if request.method =='POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect('posts')
        else:
            print(form.errors)
        
    form = BlogForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_post.html',context)

def edit_post(request,pk):
    post = get_object_or_404(Blogs, pk=pk)
    if request.method =='POST':
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
        
    form = EditPostForm(instance = post) 
    context={
        'form':form,
        'post':post,
        }

    return render(request,'dashboard/edit_post.html',context)


def delete_post(request,pk):
    post = get_object_or_404(Blogs, pk=pk)
    post.delete()
    return redirect('posts')

def users(request):
    users = User.objects.all()
    context ={
        'users':users,
    }
    return render (request, "dashboard/users.html",context)


def add_users(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = AddUserForm()
    context={
        'form':form
    }
    return render(request,'dashboard/add_users.html',context)

def edit_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method =='POST':
         form = EditUserForm(request.POST, instance = user)
         if form.is_valid():
             form.save()
             return redirect('users')
        
    form = EditUserForm(instance = user)
    context = {
        'form':form,
        'user':user,
    }
    return render(request,'dashboard/edit_user.html',context)

def delete_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')
