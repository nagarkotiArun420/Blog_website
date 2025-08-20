from django.shortcuts import redirect, render
from blog_main import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


# Create your views here.

def registration(request):
    
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration')
    else:  
        form = forms.RegistrationForm()
    context = {
        'form': form,
    }
    
    return render(request,'registration.html',context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            
    else:
        
        form = AuthenticationForm()
    context = {
        'form' : form,
    } 
    return render(request,"login.html", context)


def logout (request):
    auth.logout(request)
    return redirect('home')