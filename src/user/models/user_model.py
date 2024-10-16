from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    role = models.CharField(choices=[('client', 'Client'), ('freelancer', 'Freelancer')], max_length=50)
    photo = models.ImageField(upload_to='users/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None or 'password' in self.__dict__:
            if self.password and not self.password.startswith('pbkdf2_'):
                self.set_password(self.password)
        super(UserModel, self).save(*args, **kwargs)

    def set_password(self, raw_password):
        super().set_password(raw_password)
