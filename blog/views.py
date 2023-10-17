from django.shortcuts import render

def index(request):
    return render(request, 'blog\index.html')

def about(request):
    return render(request, 'blog\_about.html')

def contact(request):
    return render(request, 'blog\contact.html')

def blog_home(request):
    return render(request, 'blog\Blog_home.html')

def blog_single(request):
    return render(request, 'blog\Blog_single.html')