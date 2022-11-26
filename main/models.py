from django.db import models

class Password(models.Model):
    password = models.CharField(max_length=20)
    tag = models.CharField(max_length=10)