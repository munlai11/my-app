# Generated by Django 2.2.2 on 2019-06-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20190623_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpart',
            name='question_number',
            field=models.IntegerField(default=0),
        ),
    ]
