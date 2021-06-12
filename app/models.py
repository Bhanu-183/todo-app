from django.db import models
from django import forms
# Create your models here.

class Clients(models.Model):
    username=models.CharField(null=True,blank=False,max_length=32)
    password = models.CharField(max_length=32,null=True,blank=False)
    email=models.CharField(null=True,blank=False,max_length=32)

    def __str__(self):
        return self.username

class Task(models.Model):
    user=models.ForeignKey(Clients,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete']