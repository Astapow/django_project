# Generated by Django 4.2 on 2023-04-17 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_blogpost_comment_topic_alter_article_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]