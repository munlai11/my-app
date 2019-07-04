from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.widgets import SelectDateWidget, SplitDateTimeWidget, TimeInput

def user_directory_path(instance, filename):

    return 'images/{0}/{1}/'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, help_text="Bio")
    dob = models.DateField(null=True, blank=True)
    skype = models.CharField(max_length=100, blank=True, help_text="Skype (Only used for practice interviews)")
    created_date = models.DateTimeField(default=timezone.now)
    pic = models.ImageField(upload_to=user_directory_path,null=True, blank=True, help_text="Profile Picture")

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



