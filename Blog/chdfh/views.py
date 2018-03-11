from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,"index.html")

@login_required()
def blog(request):
    return render(request,"blog.html")

@login_required()
def portfolio(request):
    return render(request,"portfolio.html")

@login_required()
def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

