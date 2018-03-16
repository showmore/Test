from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
import markdown
from .models import *
from .files import get_picfiles

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

def picpage(request):
    blog = Blog.objects.first()
    blog_content = markdown.markdown(blog.content)
    return render(request,"picpage.html",locals())

def AD(request):
    ad = AlcoholDetection.objects.all()
    pics = get_picfiles()
    return render(request,"AlcoholDetection.html",locals())