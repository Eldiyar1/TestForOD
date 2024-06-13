from django.db import models
from apps.users.models import User


class Enterprise(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    location = models.CharField(max_length=100, verbose_name="Местоположение")
    work_hours = models.CharField(max_length=100, verbose_name="Часы работы")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enterprises', verbose_name='Пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='products',
                                   verbose_name='предприятие')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
