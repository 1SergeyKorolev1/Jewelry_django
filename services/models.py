from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}
materials = {
    'gold': 'Золото',
    'silver': 'Серебро',
    'platinum': 'Платина',
}


class Sale(models.Model):
    material = models.CharField(
        max_length=150,
        verbose_name='выберите материал',
        help_text='',
        choices=materials,
        error_messages='Поле обязательно для заполнения'
    )
    weight = models.FloatField(
        verbose_name='вес в граммах',
        help_text='',
        error_messages='Укажите вес изделия в граммах'
    )
    result = models.FloatField(
        verbose_name='результат',
        default=0,
        **NULLABLE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='укажите владельца',
        verbose_name='владелец',
        **NULLABLE
    )

    def __str__(self):
        # Строковое отображение объекта
        return f'Материал: {self.material}\nВес: {self.weight}г.'

    class Meta:
        verbose_name = 'Продажа'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Продажи'  # Настройка для наименования набора объектов
