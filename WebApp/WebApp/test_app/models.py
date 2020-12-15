from django.db import models

# Create your models here.


class TestClass(models.Model):
    counter = models.IntegerField(default=0)

