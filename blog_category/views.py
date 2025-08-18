from django.http import HttpResponse
from django.shortcuts import render

from blog_category.models import Blogs

# Create your views here.
def posts_by_category(request, category_id):
    
    #fetch the post that belongs to the category
    posts = Blogs.objects.filter(status="published", category = category_id)
    
    context = {
        'posts':posts
    }
    return render(request, 'posts_by_category.html',context)