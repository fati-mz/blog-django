from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [

    path('', views.blog_home, name='index'),
    path('<int:p_id>', views.blog_single, name='blog_single'),
    path('category/<str:category_name>', views.blog_home, name='category'),
    path('tag/<str:tag_name>', views.blog_home, name='tag'),
    path('author/<str:author_username>', views.blog_home, name='author'),
    path('search/',views.blog_search, name='search'),

]
