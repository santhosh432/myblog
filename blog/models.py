from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    posted_date = models.DateTimeField(default=timezone.now())
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{0}'.format(self.title)