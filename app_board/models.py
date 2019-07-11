from django.db import models
from django.conf import settings
from django.utils import timezone
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



    
