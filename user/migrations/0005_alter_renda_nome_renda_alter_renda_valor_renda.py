# Generated by Django 5.1.1 on 2024-10-20 20:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_despesa_parcelas_alter_despesa_valor_despesa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renda',
            name='nome_renda',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='renda',
            name='valor_renda',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
