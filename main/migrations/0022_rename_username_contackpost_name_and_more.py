# Generated by Django 4.2.1 on 2023-05-11 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_contackpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contackpost',
            old_name='username',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contackpost',
            old_name='usersurname',
            new_name='surname',
        ),
    ]
