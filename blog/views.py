from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    post = Post.objects.filter(published_at__lte=timezone.now())
    context = {'posts': post}
    return render(request, 'blog\index.html', context)


def about(request):
    post = Post.objects.filter(status=1)
    context = {'posts': post}
    return render(request, 'blog\About.html', context)


def contact(request):
    post = Post.objects.filter(status=1)
    context = {'posts': post}
    return render(request, 'blog\contact.html', context)


def blog_home(request):
    post = Post.objects.filter(status=1)
    context = {'posts': post}
    return render(request, 'blog\Blog_home.html', context)


def blog_single(request,p_id):
    post = get_object_or_404(Post,pk=p_id,status=1)
    post.counted_views+=1
    post.save()
    context = {'post': post}
    
    return render(request, 'blog\Blog_single.html', context)
