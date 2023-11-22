from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=127,
                            validators=[MinLengthValidator(3, "Name must be greater than 2 characters")])

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=127,
                            validators=[MinLengthValidator(3, "Name must be greater than 2 characters")])

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255,
                             validators=[MinLengthValidator(2, "Title must be greater than 2 characters")])
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    counted_views = models.IntegerField(null=True, default=0)
    status = models.BooleanField(default=False,)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_single', kwargs={'p_id': self.id})
