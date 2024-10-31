from django_resized import ResizedImageField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
from config.settings import AUTH_USER_MODEL

NULLABLE = {'blank': True, 'null': True}
_MAX_SIZE = 300

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='почта',
        error_messages='Укажите действующий email на него придет сообщение с ссылкой для подтверждения'
    )

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = ResizedImageField(
        size=[300, 300],
        quality=77,
        upload_to='users/avatars/',
        verbose_name='аватар',
        **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)

    token = models.CharField(max_length=150, verbose_name='токен', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def unique_error_message(self, model_class, unique_check):
        return 'Пользователь с такой почтой уже зарегистрирован!..'

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Пользователи'  # Настройка для наименования набора объектов
