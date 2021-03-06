# Generated by Django 2.2 on 2020-08-02 10:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('food', 'Еда'), ('tech', 'Бытовая техника'), ('tools', 'Инструменты'), ('other', 'Разное'), ('toys', 'Игрушки')], default='other', max_length=20, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
    ]
