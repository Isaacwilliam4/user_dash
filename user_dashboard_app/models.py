from django.db import models
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['email'])< 1:
            errors['email'] = 'Email is required'

        if len(post_data['first_name'])< 1:
            errors['first_name'] = 'First Name is required'

        if len(post_data['last_name'])< 1:
            errors['last_name'] = 'Last Name is required'

        if len(post_data['password'])< 1:
            errors['password'] = 'Password is required'
        elif len(post_data['password'])<8:
            errors['password'] = 'Password must be at least 8 characters'

        if post_data['password'] != post_data['confirm']:
            errors['confirm'] = 'Passwords do not match'

        return errors

    def admin_edit_user(self, post_data):
        errors = {}

        if len(post_data['email'])< 1:
            errors['email'] = 'Email is required'

        if len(post_data['first_name'])< 1:
            errors['first_name'] = 'First Name is required'

        if len(post_data['last_name'])< 1:
            errors['last_name'] = 'Last Name is required'
        return errors
    
    def admin_edit_password(self, post_data):
        errors = {}
        if len(post_data['password'])< 1:
            errors['password'] = 'Password is required'
        elif len(post_data['password'])<8:
            errors['password'] = 'Password must be at least 8 characters'

        if post_data['password'] != post_data['confirm']:
            errors['confirm'] = 'Passwords do not match'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    user_lvl = models.IntegerField()
    desc = models.TextField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # messages_from = messages that are from this user
    # messages_for - messages that are for this user
    # comments_from = comments that are from this user
    # comments_for - comments that are for this user
    


class Message(models.Model):
    message = models.TextField()
    from_user = models.ForeignKey(User, related_name='messages_from', on_delete=models.CASCADE)
    for_user = models.ForeignKey(User, related_name='messages_for', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comments = comments that belong to this message

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)