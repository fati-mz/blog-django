# Generated by Django 4.2.6 on 2023-10-18 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at'], 'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='counted_views',
        ),
    ]
