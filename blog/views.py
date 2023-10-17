from django.shortcuts import render

def g(request):
    return render(request, 'blog\index.html')

def f(request):
    return render(request, 'blog\_about.html')
def d(request):
    return render(request, 'blog\contact.html')
