# Generated by Django 5.1.1 on 2024-10-20 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='nome_despesa',
            field=models.CharField(default='Desconhecido', max_length=50),
            preserve_default=False,
        ),
    ]
