from django.shortcuts import render
from blog_category.models import Blogs, Category




# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured=True)
    posts = Blogs.objects.filter(is_featured=False, status='published')
    
    
    
    context={
        'categories':categories,
        'featured_post':featured_post,
        'posts': posts,
    }
    return render(request,'home.html',context)


