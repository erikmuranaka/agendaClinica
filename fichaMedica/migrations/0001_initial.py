# Generated by Django 5.2 on 2025-04-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fichaMedica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('descricao', models.TextField()),
            ],
        ),
    ]
