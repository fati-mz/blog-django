from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.forms import ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request, 'home/index.html')


def about_view(request):
    return render(request, 'home/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'your ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR,
                                 'your ticket didnt submited')
    form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'home/index.html')
