# Generated by Django 5.2 on 2025-04-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0002_alter_fornecedor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='dataCadastro',
            field=models.DateTimeField(auto_now_add=True, default='2025-04-17'),
            preserve_default=False,
        ),
    ]
