# Generated by Django 2.2.2 on 2019-06-22 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the posts's company (e.g. Google, Microsoft etc.)", max_length=200)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the posts's industry (e.g. technology, banking etc.)", max_length=200)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questions.Company')),
                ('industry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questions.Industry')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the posts's role (e.g. software engineering, trading etc.)", max_length=200)),
                ('slug', models.SlugField(blank=True)),
                ('industry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questions.Industry')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('question_part', models.TextField()),
                ('answer_part', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_parts', to='questions.Question')),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questions.Role'),
        ),
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questions.Industry'),
        ),
    ]