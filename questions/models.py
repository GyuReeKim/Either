from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    option_left = models.CharField(max_length=50)
    option_right = models.CharField(max_length=50)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.TextField()
