from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    pass

    def save(self, *args, **kwargs):
        if self.pk is None or 'password' in self.__dict__:
            if self.password and not self.password.startswith('pbkdf2_'):
                self.set_password(self.password)
        super(UserModel, self).save(*args, **kwargs)

    def set_password(self, raw_password):
        super().set_password(raw_password)
