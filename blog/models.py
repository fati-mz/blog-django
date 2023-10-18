from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from datetime import datetime


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
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    #                            related_name='favs_users')
    # image = models.BinaryField(null=True, editable=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    counted_views = models.IntegerField(null=True, default=0)
    status = models.BooleanField(default=False,)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
