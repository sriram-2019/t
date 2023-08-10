from django.db import models

# Create your models here.
class mod(models.Model):
    username=models.CharField(max_length=264)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return (self.username,self.password,self.email)