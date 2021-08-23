from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=100000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    image = models.ImageField(upload_to = 'images')
    video_url = models.CharField(max_length=500,blank=True)
    tweeter_url = models.CharField(max_length=500,blank=True)

    def __str__(self) -> str:
        return f'{self.title}-{self.body}'

