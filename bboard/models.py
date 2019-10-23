from django.db import models
from django.core import validators
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


@python_2_unicode_compatible
class Bb(models.Model):
    KINDS = (
        ('None', 'Выберите разряд публикуемого обьявленя'),
        ('Куплю', 'Куплю'),
        ('Продам', 'Продам'),
        ('Обменяю', 'Обменяю'),
    )
    kind = models.CharField(max_length=10, choices=KINDS, default=True, verbose_name='Сортировка')
    title = models.CharField(max_length=50, verbose_name='Товар',
                             validators=[validators.RegexValidator(regex='^.{4,}$')],
                             error_messages={'invalid': 'Неправильно называние товара'},
                             unique_for_date='published')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(null=True, blank=True, verbose_name='Цена', max_digits=20000000, decimal_places=2)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        unique_together = (
            ('title', 'published'),
            ('title', 'price')
        )
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published', 'title']

    def __str__(self):
        return self.title


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Называние')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['-name']

    def __str__(self):
        return self.name

# как ссылка на функцию, вызываемую при создании каждой новой записи
# и возвращающую в качестве результата нужное значение:
def is_active_default():
    return not is_all_posts_passive


is_active = models.BooleanField(default=is_active_default)


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name = models.CharField(max_length=30, verbose_name='Называния детали')


class Machine(models.Model):
    name = models.CharField(max_length=30, verbose_name='Называния машина')
    spares = models.ManyToManyField(Spare)


def validate_even(val):
    if val % 2 != 0:
        raise ValidationError('Число % (value) s нечетнoе', code='odd',
                              params={'value': val})


class MinMaxValueValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, val):
        if val < self.min_value or val > self.max_value:
            raise ValidationError('Введенное число должно ' +\
                                  ' находиться в диапозоне от % (min)s до %(max)s',
                                  code='out_of _range',
                                  params={'min': self.min_value, 'max': self.max_value})

