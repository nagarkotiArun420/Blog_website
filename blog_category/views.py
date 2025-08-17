from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def posts_by_category(request, categroy_id):
    return HttpResponse("post by category")