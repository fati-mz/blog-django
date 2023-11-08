from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [

    path('blog_home/', views.blog_home, name='blog_home'),
    path('blog_single/<int:p_id>', views.blog_single, name='blog_single'),
    path('category/<str:category_name>', views.blog_home, name='category'),
    path('author/<str:author_username>', views.blog_home, name='author'),
    path('search/',views.blog_search, name='search'),

]
