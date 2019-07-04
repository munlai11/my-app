from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from categories.models import Industry, Role, Company
from django.db.models import Max
import random

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,help_text="Title")
    text = models.TextField(max_length=300,help_text="Text")
    created_date = models.DateTimeField(default=timezone.now)
    industry = models.ForeignKey('categories.Industry', on_delete=models.SET_NULL, null=True,help_text="Industry")
    role = models.ForeignKey('categories.Role', on_delete=models.SET_NULL, null=True,help_text="Role")
    company = models.ForeignKey('categories.Company', on_delete=models.SET_NULL, null=True,help_text="Company")
    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering=['created_date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300,help_text="Text")
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name = 'comment_likes', blank = True)

    class Meta:
        ordering=['created_date']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.text

def get_random_post():
    max_id = Post.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        post = Post.objects.filter(pk=pk).first()
        if post:
            return post


