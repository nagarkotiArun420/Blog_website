from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.db.models import Q
from blog_category.models import Blogs, Category, Comment

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
  if request.method == "POST":
    comment = Comment()
    comment.user = request.user
    comment.blog = single_post
    comment.comment = request.POST['comment']
    comment.save()
    return HttpResponseRedirect(request.path_info)
  comments = Comment.objects.filter(blog = single_post)
  comment_count = comments.count()
  context = {
    'single_post' : single_post,
    'comments':comments,
    'comment_count':comment_count,
  }
  return render(request, 'blogs.html', context)


def search(request):
  keyword = request.GET.get('keyword')
  blog = Blogs.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
  context={
    'blogs':blog ,
    'keyword': keyword,
  }
  return render(request,'search.html',context)
  
   
  