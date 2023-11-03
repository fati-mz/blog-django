from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog_home', views.blog_home, name='blog_home'),
    path('blog_single/<int:p_id>', views.blog_single, name='blog_single'),
    path('category/<str:category_name>', views.blog_home, name='category'),
    path('author/<str:author_username>', views.blog_home, name='author'),

]
