from django.db import models

# Create your models here.

class JournalEntry(models.Model):
    title = models.CharField(max_length= 100)
    text = models.TextField()
    creationDate = models.DateTimeField('date published')