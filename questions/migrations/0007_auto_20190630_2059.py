# Generated by Django 2.2.2 on 2019-06-30 19:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0006_question_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='completed',
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='question_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]