from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('home/index_latest_post.html')
def index_latestposts(arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_at')[:arg]
    return {'posts': posts}
