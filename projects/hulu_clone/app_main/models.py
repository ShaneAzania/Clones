from distutils.log import error
from django.db import models
import bcrypt
import re

class User_Manager(models.Manager):
    def signup_validator(self, postData):
        errors = {}
        
        # check email format
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']): # test whether a field matches the pattern            
            errors['email'] = "Invalid email address format."
        # check the lengths of the passwords, first_name, and last_name
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name not long enough.'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name not long enough.'
        if len(postData['password']) < 8:
            errors['password_length'] = 'Password not long enough.'
        # check if password matches pasword2
        if postData['password'] != postData['password2']:
            errors['password'] = "Password does not match."

        if len(errors) > 0:
            return errors
        else:
            return False
class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  # watchlist = list of books associated with author
    objects = User_Manager()
class Media(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    file_location = models.CharField(max_length=255)
    watcher = models.ForeignKey(User, related_name="watchlist", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
