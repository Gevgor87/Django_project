# Generated by Django 4.2.1 on 2023-05-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Home image')),
                ('price', models.PositiveIntegerField(verbose_name='Home price')),
                ('discount', models.PositiveIntegerField(verbose_name='Home discount')),
            ],
        ),
    ]
