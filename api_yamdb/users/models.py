from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from api.validators import username_validator


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    ]
    email = models.EmailField(
        'Электронная почта',
        max_length=settings.MAX_LENGHT_EMAIL, unique=True
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        unique=True,
        max_length=settings.MAX_LENGHT_USERNAME,
        validators=(username_validator,),
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль пользователя',
        max_length=max(len(role) for role, _ in ROLE_CHOICES),
        choices=ROLE_CHOICES,
        default=USER,
    )
    first_name = models.CharField(
        'Имя', max_length=settings.MAX_LENGHT_USERNAME, blank=True
    )
    last_name = models.CharField(
        'Фамилия', max_length=settings.MAX_LENGHT_USERNAME, blank=True
    )
    confirmation_code = models.CharField(
        'Код подверждения',
        blank=True,
        null=True,
        max_length=settings.MAX_LENGHT_CODE
    )

    class Meta:
        ordering = ('id',)

    @property
    def is_admin(self):
        return (
            self.role == 'admin'
            or self.is_superuser
            or self.is_staff
        )

    def __str__(self):
        return self.username

    @property
    def is_moderator(self):
        return self.role == 'moderator'
