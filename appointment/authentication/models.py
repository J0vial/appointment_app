from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class additionalUserInfo(models.Model):
    gnd = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    cat = (
        ('Doctor','Doctor'),
        ('patient','patient'),
        
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    catagory = models.CharField(choices=cat,max_length=50)
    gender = models.CharField(choices=gnd,max_length=30)
    Phone_no = models.CharField(max_length=11)
    
    def __str__(self):
        return self.user.username
    
