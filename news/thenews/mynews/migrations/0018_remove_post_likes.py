# Generated by Django 3.2.4 on 2021-06-04 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mynews', '0017_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
