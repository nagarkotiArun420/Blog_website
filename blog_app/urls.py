from blog_app import views
from django.urls import include, path


urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('home',views.home, name='home'),
    

]
