from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from categories.models import Industry, Role, Company, Difficulty
from accounts.models import Profile

class Interview(models.Model):

    title = models.CharField(max_length=50,help_text="Title")
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="author")
    partner = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name="partner")
    notes = models.CharField(max_length=50, help_text="Notes")
    created_date = models.DateTimeField(default=timezone.now)
    interview_date = models.DateField(default=timezone.now)
    interview_time = models.TimeField(default= timezone.now)
    industry = models.ForeignKey('categories.Industry', on_delete=models.SET_NULL, null=True,help_text="Industry")
    role = models.ForeignKey('categories.Role', on_delete=models.SET_NULL, null=True,help_text="Role")
    company = models.ForeignKey('categories.Company', on_delete=models.SET_NULL, null=True,help_text="Company")
    accepted = models.BooleanField(default=False)
    difficulty = models.ForeignKey('categories.Difficulty', on_delete=models.SET_NULL, null=True,help_text="Level")
    slug = models.SlugField(blank=True)

    class Meta:
        ordering=['-interview_date']

    def __str__(self):
        return self.title

    def accept(self):  
        self.accepted = True
        self.save()

    def cancel(self):
        self.partner = None
        self.accepted = False
        self.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Interview, self).save(*args, **kwargs)

