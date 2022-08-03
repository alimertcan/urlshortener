from django.db import models
import random
import string
# Create your models here.

def generate_link():
    return ''.join([random.choice(string.ascii_letters) for _ in range(6)])

class Url(models.Model):
    real_url = models.URLField(max_length=255)
    generated_url = models.CharField(max_length=255,unique=True,default=generate_link())
    view_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)



