from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


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

class Difficulty(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the difficulty")
    slug = models.SlugField(blank=True)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Difficulty, self).save(*args, **kwargs)
