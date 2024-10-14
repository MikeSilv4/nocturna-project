from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from simple_history.models import HistoricalRecords

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('O campo de e-mail deve ser definido')

        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):

    username = models.CharField(max_length=512, null=False)
    email = models.CharField(max_length=512, null=False, unique=True)
    born_date = models.DateField(null=True)
    cpf = models.CharField(max_length=14, null=True)
    history = HistoricalRecords()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()