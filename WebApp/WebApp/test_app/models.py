from django.db import models

# Create your models here.


class TestClass(models.Model):
    text = models.CharField(null=False)


