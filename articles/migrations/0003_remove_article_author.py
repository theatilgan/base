# Generated by Django 3.1.4 on 2020-12-29 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]