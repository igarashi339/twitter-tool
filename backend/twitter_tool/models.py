from django.db import models


class User(models.Model):
    username = models.CharField(max_length=16)
    name = models.CharField()
    status = models.CharField()