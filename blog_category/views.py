from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect

from blog_category.models import Blogs, Category

# Create your views here.
def posts_by_category(request, category_id):
    
    #fetch the post that belongs to the category
    posts = Blogs.objects.filter(status="published", category = category_id)
    
    try:
      category = Category.objects.get(pk=category_id)
    except:
      return redirect('home')
    
    # category = get_object_or_404(Category, pk = category_id)
    
    context = {
        'posts':posts,
        'category':category,
        
    }
    return render(request, 'posts_by_category.html',context)
  
  
def blogs(request, slug):
  single_post = get_object_or_404(Blogs, slug=slug, status = 'published')
  context = {
    'single_post' : single_post,
  }
  return render(request, 'blogs.html', context)
  
   
  