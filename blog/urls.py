from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name='blog'
urlpatterns = [
    path('', views.g, name='index'),
    path('about/', views.f, name='about'),
    path('contact', views.d, name='contact'),

    # path('a/', TemplateView.as_view(template_name='about.html'))

]