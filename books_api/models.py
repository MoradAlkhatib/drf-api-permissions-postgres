from django.db import models

from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(User,on_delete=models.CASCADE) 
    description = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
