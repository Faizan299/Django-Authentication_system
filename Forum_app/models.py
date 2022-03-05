from django.db import models
from django.urls import reverse
from django.conf import settings


class forum(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    topic = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.topic
    
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=100)
    
    def __str__(self):
        return self (self.forum)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forum = models.ForeignKey(forum, on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('forum-list')

