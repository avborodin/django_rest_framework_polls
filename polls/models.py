import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Poll(models.Model):
    name = models.CharField(max_length=128)
    start_dt = models.DateField()
    end_dt = models.DateField()
    descr = models.TextField(max_length=512)

class QuestionType(models.Model):
	text = models.CharField(max_length=128)

class Question(models.Model):
	poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
	text = models.CharField(max_length=256)
	questtype = models.ForeignKey('QuestionType', on_delete=models.CASCADE)

class Vote(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	date = models.DateField(default=datetime.date.today(), editable=False)

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	vote = models.ForeignKey(Vote, related_name='answers', on_delete=models.CASCADE)
	questtype = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
	value = models.CharField(max_length=128, blank=True, null=True)
