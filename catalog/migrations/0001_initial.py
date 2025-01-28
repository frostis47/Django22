import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Здесь можно указать зависимости, если есть другие миграции
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    max_length=250,
                    verbose_name='название',
                    help_text='Введите название',
                    blank=True,
                    null=True
                )),
                ('description', models.TextField(
                    max_length=250,
                    verbose_name='описание',
                    help_text='Введите описание',
                    blank=True,
                    null=True
                )),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    max_length=250,
                    verbose_name='название',
                    help_text='Введите название'
                )),
                ('description', models.TextField(
                    verbose_name='описание',
                    help_text='Введите описание'
                )),
                ('image', models.ImageField(
                    upload_to='media/photo',
                    verbose_name='фото',
                    help_text='Загрузить фотографию',
                    blank=True,
                    null=True
                )),
                ('price', models.CharField(
                    max_length=100,
                    verbose_name='Цена',
                    help_text='Введите цену',
                    blank=True,
                    null=True
                )),
                ('created_at', models.DateField(
                    verbose_name='дата создания',
                    help_text='Введите дату создания',
                    blank=True,
                    null=True
                )),
                ('updated_at', models.DateTimeField(
                    auto_now=True,
                    verbose_name='дата последнего изменения'
                )),
                ('category', models.ForeignKey(
                    to='catalog.category',
                    on_delete=django.db.models.deletion.CASCADE,
                    verbose_name='категория',
                    help_text='Введите категорию',
                    blank=True,
                    null=True
                )),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]


