from django.shortcuts import redirect, render
from blog_main import forms


# Create your views here.

def registration(request):
    
    if request == "POST":
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
    
    
    return render(request,"login.html")