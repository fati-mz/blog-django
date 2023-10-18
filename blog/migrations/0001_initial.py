# Generated by Django 4.2.6 on 2023-10-18 08:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, validators=[django.core.validators.MinLengthValidator(3, 'Name must be greater than 2 characters')])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2, 'Title must be greater than 2 characters')])),
                ('content', models.TextField()),
                ('counted_views', models.IntegerField(default=0, null=True)),
                ('status', models.BooleanField(default=False)),
                ('published_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, validators=[django.core.validators.MinLengthValidator(3, 'Name must be greater than 2 characters')])),
            ],
        ),
    ]