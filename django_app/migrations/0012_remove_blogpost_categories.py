# Generated by Django 4.2 on 2023-04-22 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0011_alter_comment_blog_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='categories',
        ),
    ]
