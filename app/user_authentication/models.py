from django.db import models
from ast import mod
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

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

    objects = CustomUserManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []

 

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

