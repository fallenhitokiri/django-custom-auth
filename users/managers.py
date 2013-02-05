# -*- coding: utf-8 -*-
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('No email!')
        email = BaseUserManager.normalize_email(email)
        user = self.model(email=email, is_superuser=False, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError('No email!')
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user