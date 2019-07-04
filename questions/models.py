from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from categories.models import Industry, Role, Company, Difficulty
from django.db.models import Max
import random

class Question(models.Model):
    title = models.CharField(max_length=200,help_text="Title")
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    difficulty = models.ForeignKey('categories.Difficulty', on_delete=models.SET_NULL, null=True,help_text="Difficulty")
    industry = models.ForeignKey('categories.Industry', on_delete=models.SET_NULL, null=True,help_text="Industry")
    role = models.ForeignKey('categories.Role', on_delete=models.SET_NULL, null=True,help_text="Role")
    company = models.ForeignKey('categories.Company', on_delete=models.SET_NULL, null=True,help_text="Company")
    likes = models.ManyToManyField(User,related_name = "question_likes", blank = True)
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class QuestionPart(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='question_parts')
    question_number = models.IntegerField(default = 0)
    question_part = models.TextField(help_text="Question")
    answer_part = models.TextField(help_text="Answer")
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
        
    class Meta:
        ordering=['created_date']
        
    def __str__(self):
        return self.question_part

def get_random_question():
    max_id = Question.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        question = Question.objects.filter(pk=pk).first()
        if question:
            return question
