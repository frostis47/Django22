from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Создает и возвращает пользователя с электронной почтой и паролем."""
        if not email:
            raise ValueError('Пользователь должен иметь адрес электронной почты')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создает и возвращает суперпользователя с электронной почтой и паролем."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Эл.почта")
    avatar = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватар',
                               help_text='Загрузите фотографию')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', help_text='Введите номер телефона', blank=True, null=True)
    country = models.CharField(max_length=40, verbose_name="Страна", blank=True, null=True,
                               help_text="Введите страну проживания")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = "Пользователи"
