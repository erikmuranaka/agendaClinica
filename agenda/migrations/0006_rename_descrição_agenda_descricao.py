# Generated by Django 5.2 on 2025-04-24 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_alter_agenda_descrição'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='descrição',
            new_name='descricao',
        ),
    ]
