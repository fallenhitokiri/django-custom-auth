from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.managers import CustomUserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address',max_length=254, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
 
    def get_full_name(self):
        return self.email
 
    def get_short_name(self):
        return self.email
