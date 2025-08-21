
from dashboard import views 

from django.urls import path


urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('dashboard/categories/', views.categories, name="categories"),
    path('dashboard/categories/add', views.add_categories, name="add_categories"),
    path('dashboard/categories/edit/<int:pk>', views.edit_categories, name="edit_categories"),
    path('dashboard/categories/delete/<int:pk>', views.delete_categories, name="delete_categories"),
    path('dashboard/posts/', views.posts, name="posts"),\
    path('dashboard/posts/add/', views.add_post, name="add_post"),
    path('dashboard/posts/edit/<int:pk>', views.edit_post, name="edit_post"),
    path('dashboard/posts/delete/<int:pk>', views.delete_post, name="delete_post"),

    
    path('dashboard/users/', views.users, name="users"),
    path('dashboard/users/add', views.add_users, name="add_users"),
    path('dashboard/users/edit/<int:pk>', views.edit_user, name="edit_user"),
    path('dashboard/users/delete/<int:pk>', views.delete_user, name="delete_user"),
    
]
