# Generated by Django 4.2.7 on 2024-11-17 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_view', 'Can view book'), ('can_create', 'Can create book'), ('can_edit', 'Can edit book'), ('can_delete', 'Can delete book')]},
        ),
    ]
