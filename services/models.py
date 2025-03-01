from django.db import models
from django_resized import ResizedImageField

from users.models import User

NULLABLE = {'blank': True, 'null': True}
materials = {
    'gold': 'Золото',
    'silver': 'Серебро',
    'platinum': 'Платина',
}
gold_samples = {
    'none': 'неизвестно',
    '999': '999',
    '958': '958',
    '900/916': '900/916',
    '850': '850',
    '750': '750',
    '583/585': '583/585',
    '500/555': '500/555',
    '375': '375',
}
silver_samples = {
    'none': 'неизвестно',
    '999': '999',
    '925': '925',
    '900': '900',
    '875': '875',
    '800': '800',
    '750': '750',
    '600': '600',
}
platinum_samples = {
    'none': 'неизвестно',
    '999': '999',
    '950': '950',
    '900': '900',
    '850': '850',
    '800': '800',
}

class Other(models.Model):
    material = models.CharField(
        default=materials['gold'],
        max_length=150,
        verbose_name='выберите материал',
        help_text='',
        choices=materials,
        error_messages='Поле обязательно для заполнения'
    )
    description = models.TextField(
        verbose_name='Опишите проблему / Прокомментируйте заказ',
        max_length=300
    )
    image_one = ResizedImageField(
        verbose_name='фото 1',
        size=[600, 600],
        quality=88,
        upload_to='users/repair/',
        **NULLABLE
    )
    image_two = ResizedImageField(
        verbose_name='фото 2',
        size=[600, 600],
        quality=88,
        upload_to='users/repair/',
        **NULLABLE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='укажите владельца',
        verbose_name='владелец',
        **NULLABLE
    )
    number = models.CharField(
        max_length=100,
        verbose_name='номер заказа',
        **NULLABLE
    )

    def __str__(self):
        return f'Материал: {self.material}.'

    class Meta:
        verbose_name = 'Другое'
        verbose_name_plural = 'Другое'

class Repair(models.Model):
    material = models.CharField(
        default=materials['gold'],
        max_length=150,
        verbose_name='выберите материал',
        help_text='',
        choices=materials,
        error_messages='Поле обязательно для заполнения'
    )
    description = models.TextField(
        verbose_name='Опишите проблему / Прокомментируйте заказ',
        max_length=300
    )
    image_one = ResizedImageField(
        verbose_name='фото вашего изделия',
        size=[600, 600],
        quality=88,
        upload_to='users/repair/',
    )
    image_two = ResizedImageField(
        verbose_name='фото вашего изделия',
        size=[600, 600],
        quality=88,
        upload_to='users/repair/',
        **NULLABLE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='укажите владельца',
        verbose_name='владелец',
        **NULLABLE
    )
    number = models.CharField(
        max_length=100,
        verbose_name='номер заказа',
        **NULLABLE
    )

    def __str__(self):
        # Строковое отображение объекта
        return f'Материал: {self.material}.'

    class Meta:
        verbose_name = 'Ремонт'
        verbose_name_plural = 'Ремонт'


class Sale(models.Model):
    material = models.CharField(
        default=materials['gold'],
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
    sample_gold = models.CharField(
        default=gold_samples['none'],
        max_length=150,
        verbose_name='выберите пробу золота',
        help_text='',
        choices=gold_samples,
        error_messages='Поле обязательно для заполнения'
    )
    sample_silver = models.CharField(
        default=silver_samples['none'],
        max_length=150,
        verbose_name='выберите пробу серебра',
        help_text='',
        choices=silver_samples,
        error_messages='Поле обязательно для заполнения'
    )
    sample_platinum = models.CharField(
        default=platinum_samples['none'],
        max_length=150,
        verbose_name='выберите пробу платины',
        help_text='',
        choices=platinum_samples,
        error_messages='Поле обязательно для заполнения'
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
    number = models.CharField(
        max_length=100,
        verbose_name='номер заказа',
        **NULLABLE
    )

    @staticmethod
    def sample(sample_gold, sample_silver, sample_platinum):
        if sample_gold == 'none' and sample_silver == 'none' and sample_platinum == 'none':
            return 'неизвестно'
        if sample_gold == 'none' and sample_silver == 'none':
            return sample_platinum
        if sample_silver == 'none' and sample_platinum == 'none':
            return sample_gold
        if sample_gold == 'none' and sample_platinum == 'none':
            return sample_silver
        return ''

    def __str__(self):
        # Строковое отображение объекта
        return f'Материал: {self.material}.\nВес: {self.weight}г.\nПроба: {self.sample(self.sample_gold,
                                                                                       self.sample_silver,
                                                                                       self.sample_platinum)}'

    class Meta:
        verbose_name = 'Продажа'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Продажи'  # Настройка для наименования набора объектов


class Making(models.Model):
    material = models.CharField(
        default=materials['gold'],
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
    description = models.TextField(
        verbose_name='Опишите изделие / Прокомментируйте заказ',
        max_length=300
    )
    image_one = ResizedImageField(
        verbose_name='картинка с похожим изделием',
        size=[600, 600],
        quality=77,
        upload_to='users/making/',
    )
    image_two = ResizedImageField(
        verbose_name='картинка с похожим изделием',
        size=[600, 600],
        quality=77,
        upload_to='users/making/',
        **NULLABLE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='укажите владельца',
        verbose_name='владелец',
        **NULLABLE
    )
    result = models.FloatField(
        verbose_name='результат',
        default=0,
        **NULLABLE
    )
    number = models.CharField(
        max_length=100,
        verbose_name='номер заказа',
        **NULLABLE
    )

    def __str__(self):
        # Строковое отображение объекта
        return f'Материал: {self.material}.\nВес: {self.weight}г.'

    class Meta:
        verbose_name = 'Изготовление'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Изготовление'  # Настройка для наименования набора объектов
