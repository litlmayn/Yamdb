from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    ]
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        unique=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Имя содержит недопустимый символ'
        )]
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль пользователя',
        max_length=16,
        choices=ROLE_CHOICES,
        default=USER,
    )
    confirmation_code = models.CharField(
        'Код подверждения',
        blank=True,
        null=True,
        max_length=150)

    class Meta:
        ordering = ('id',)
