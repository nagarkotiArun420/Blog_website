from django.shortcuts import render
from blog_category.models import Category,Blogs
from django.contrib.auth.decorators import login_required

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