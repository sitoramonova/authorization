import random
import string
from django.db import models

class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=6, unique=True, blank=True, null=True)
    activated_invite = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='referrals')

    def save(self, *args, **kwargs):
        if not self.invite_code:
            self.invite_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        super().save(*args, **kwargs)
    def __str__(self):
        return f"User {self.phone_number} - Invite Code: {self.invite_code}"
