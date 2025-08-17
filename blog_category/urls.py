
from django.urls import path
from blog_category import views



urlpatterns =[ 
        
    path('<int:category_id>/',views.posts_by_category, name= 'posts_by_category')
]
