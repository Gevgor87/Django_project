# Generated by Django 4.2 on 2023-05-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=20, verbose_name='Shop category')),
            ],
        ),
    ]
