
#from typing_extensions import Required
from django import forms
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todos(models.Model):
    reqdate = models.DateTimeField(auto_now_add=True)
    qty = models.IntegerField()
    part = models.CharField(max_length=50)
    description = models.TextField( )
    duedate = models.DateField()
    vendor = models.CharField(max_length=50)
    refnum = models.CharField(max_length=25, )
    toapprove= models.BooleanField(default=False)
    tobill = models.BooleanField(default=False)
    datecompleted = models.DateTimeField(null=True, blank=True)
    rush = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    billed = models.BooleanField(default=False)
    approved = models.BooleanField(default=True)
    amount= models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.part 