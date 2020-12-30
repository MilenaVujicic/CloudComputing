from django.db import models

# Create your models here.


class TestClass(models.Model):
    counter1 = models.IntegerField(default=0)
    counter2 = models.IntegerField(default=0)
