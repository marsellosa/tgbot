from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=200, unique=True) #user_id
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    is_bot = models.BooleanField(default=False)
    language_code = models.CharField(max_length=8, null=True, blank=True)
    inserted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, null=True)
    inserted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return str(self.user)
    