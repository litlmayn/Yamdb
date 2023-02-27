# Generated by Django 3.2 on 2023-02-27 20:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(message='Имя содержит недопустимый символ', regex='^[\\w.@+-]+$')], verbose_name='Имя пользователя'),
        ),
    ]