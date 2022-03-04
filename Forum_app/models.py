from django.db import models

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
