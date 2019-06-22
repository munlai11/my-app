from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,help_text="Title")
    text = models.TextField(max_length=300,help_text="Text")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    industry = models.ForeignKey('Industry', on_delete=models.SET_NULL, null=True,help_text="Industry")
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True,help_text="Role")
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True,help_text="Company")
    slug = models.SlugField(blank=True)

    class Meta:
        ordering=['-created_date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    #author = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=300,help_text="Text")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering=['created_date']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Industry(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the posts's industry (e.g. technology, banking etc.)")
    slug = models.SlugField(blank=True)   

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Industry, self).save(*args, **kwargs)

class Role(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the posts's role (e.g. software engineering, trading etc.)")
    industry = models.ForeignKey('Industry', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(blank=True)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Role, self).save(*args, **kwargs)

class Company(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the posts's company (e.g. Google, Microsoft etc.)")
    industry = models.ForeignKey('Industry', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(blank=True)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)