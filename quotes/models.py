from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
    

class Meta:
        managed = False
        db_table = 'quotes_quote'
        app_label = 'quotes'
        using = 'mongodb'