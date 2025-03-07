from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='название', help_text='Введите название', blank=True, null=True)
    description = models.TextField(verbose_name='описание', help_text='Введите описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='название', help_text='Введите название')
    description = models.TextField(verbose_name='описание', help_text='Введите описание', blank=True, null=True)
    image = models.ImageField(upload_to='product/photo', blank=True, null=True, verbose_name='фото',
                              help_text='Загрузите фотографию')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория',
                                 help_text='Введите категорию', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', help_text='Введите цену', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0, verbose_name='Количество на складе', help_text='Введите количество на складе')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


