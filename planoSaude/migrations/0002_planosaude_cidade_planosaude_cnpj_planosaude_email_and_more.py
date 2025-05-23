# Generated by Django 5.2 on 2025-04-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planoSaude', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planosaude',
            name='cidade',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='planosaude',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='planosaude',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='planosaude',
            name='endereco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='planosaude',
            name='estado',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='planosaude',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='planosaude',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
