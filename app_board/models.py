from django.db import models
from django.conf import settings
from django.utils import timezone
from django import forms
# Create your models here.

class Board(models.Model) :
    title = models.CharField(max_length = 200)
    pub_date = models.DateField('date published')
    body = models.TextField()
    writer = models.CharField(max_length = 100)

    def __str__(self) :
        return self.title

    def summary(self) :
        return self.body[:100]

# class Comment(models.Model) :
#     post = models.ForeignKey(Board, on_delete = models.CASCADE, null=True, related_name='comments')
#     comment_date = models.DateField(auto_now_add = True)
#     comment_contents = models.CharField(max_length = 200)
#     comment_writer = models.CharField(max_length = 200)





    
