
# Create your models here.
from django.db import models
from user.models import SUser

import user.models

"""
 * MODEL No. 1
 * MODEL Name : Question
"""
class Question(models.Model):
    author = models.ForeignKey(SUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


    def __str__(self):          ##Question.objects.all() 실행시 id 대신 제목받아옴
        return self.subject

"""
 * MODEL No. 2
 * MODEL Name : Answer
"""
class Answer(models.Model):
    author = models.ForeignKey(SUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()