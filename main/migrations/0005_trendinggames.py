# Generated by Django 4.2.1 on 2023-05-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendingGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Trending Games image')),
                ('name', models.CharField(max_length=60, verbose_name='Trending Games name')),
                ('category', models.CharField(max_length=50, verbose_name='Trending Games category')),
                ('old_price', models.PositiveIntegerField(verbose_name='Trending Games old price')),
                ('new_price', models.PositiveIntegerField(verbose_name='Trending Games')),
            ],
        ),
    ]