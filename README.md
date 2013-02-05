This is a quick & dirty example how you can use a custom user model
in Django 1.5. 

Add `users` to `INSTALLED_APPS` and `AUTH_USER_MODEL = 'users.UserModel'`
to your `settings.py`. Sync your database and you are done.
