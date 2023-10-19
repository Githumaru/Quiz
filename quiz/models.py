from django.db import models

class Quiz(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

