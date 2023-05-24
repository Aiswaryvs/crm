from django.db import models
from ast import mod
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class User(AbstractUser):
    username=None
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)    
    address = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=12,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_active =  models.BooleanField(default=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['first_name']

 

# class Role(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     is_created = models.DateTimeField(auto_now=False, auto_now_add=True)
#     is_updated = models.DateTimeField(auto_now=False, auto_now_add=True)
#     is_active =  models.BooleanField(default=False)


# class RoleFeature(models.Model):
#     id = models.AutoField(primary_key=True)
#     role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
#     feature_id = models.ForeignKey(Feature, on_delete=models.CASCADE)
#     view = models.BooleanField(default=False)
#     edit = models.BooleanField(default=False)
#     delete = models.BooleanField(default=False)
#     create = models.BooleanField(default=False)
#     is_created = models.DateTimeField(auto_now=False, auto_now_add=True)
#     is_updated = models.DateTimeField(auto_now=False, auto_now_add=True)
#     is_active =  models.BooleanField(default=False)    

