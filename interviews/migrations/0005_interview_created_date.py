# Generated by Django 2.2.2 on 2019-06-25 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0004_auto_20190624_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]