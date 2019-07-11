from django.db import models

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

class Comment(models.Model) :
    writer = models.CharField(max_length = 200)
    content = models.CharField(max_length = 200)
    post = models.ForeignKey(Board, on_delete = models.CASCADE)
