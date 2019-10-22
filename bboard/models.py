from django.db import models
from django.core import validators
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Bb(models.Model):
    # KINDS = (
    #     ('None', 'Выберите разряд публикуемого обьявленя'),
    #     ('Куплю', 'Куплю'),
    #     ('Продам', 'Продам'),
    #     ('Обменяю', 'Обменяю'),
    # )
    # kind = models.CharField(max_length=10, choices=KINDS)
    title = models.CharField(max_length=50, verbose_name='Товар',
                             validators=[validators.RegexValidator(regex='^.{4,}$')],
                             error_messages={'invalid': 'Неправильно называние товара'},
                             unique_for_date='published')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(null=True, blank=True, verbose_name='Цена', max_digits=2000000000, decimal_places=2)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    #rubric = models.ForeignKey(null=True, verbose_name='Рубрика', on_delete=None, to=None)

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
