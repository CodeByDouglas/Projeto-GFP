# Generated by Django 5.1.1 on 2024-10-20 00:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_despesa_nome_despesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='data_despesa',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]