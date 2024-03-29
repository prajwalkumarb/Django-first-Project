from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionManager
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Manager for user profile"""
    def create_user(self , email , name , password = None):
        """Create a new user Profile"""
        if not email:
            raise ValueError('user must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self , email , name , password):
        """create and save new superuser with given details"""
        user = self.create_superuser(email , name , password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user    
class UserProfile(AbstractBaseUser,PermissionManager):
    """DataBase Model From Users in the System"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default =False)
    
    
    objects = UserProfileManager()
    
    # USERNAME_FILEDS= 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """Returns full name of user"""
        return self.name
    
    def get_short_name(self):
        """Return short name of user""" 
        return self.name
    
    def __str__(self):
        """Return string representation of out user"""
        return self.email