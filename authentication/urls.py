
from django.urls import path
from authentication import views


urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path('login/', views.login, name = "login"),
]
