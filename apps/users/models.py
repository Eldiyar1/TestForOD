from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, blank=False, null=False, unique=True, verbose_name="Имя пользователя")
    email = models.EmailField(null=True, verbose_name="Электронная почта")
    phone = PhoneNumberField(null=True, blank=False, verbose_name="Номер телефона")
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name="Пароль")
    otp = models.CharField(max_length=4, null=True, blank=True, verbose_name="Код подтверждения")
    is_active = models.BooleanField(default=False, verbose_name="Активен")
    is_staff = models.BooleanField(default=False, verbose_name="Персонал")
    is_superuser = models.BooleanField(default=False, verbose_name="Админ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
