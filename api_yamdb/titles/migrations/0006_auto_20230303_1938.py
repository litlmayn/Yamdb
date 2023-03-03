# Generated by Django 3.2 on 2023-03-03 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0005_auto_20230303_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('name',), 'verbose_name': 'Категория произведения'},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ('name',), 'verbose_name': 'Жанр произведения'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('name',), 'verbose_name': 'Произведение'},
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='сategories', to='titles.categories', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='titles', to='titles.Genres', verbose_name='Жанр'),
        ),
    ]
