# Generated by Django 4.2.1 on 2023-05-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_trendinggames_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='MostPlayed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Trending Games image')),
                ('name', models.CharField(max_length=60, verbose_name='Trending Games name')),
                ('category', models.CharField(max_length=50, verbose_name='Trending Games category')),
                ('old_price', models.PositiveIntegerField(verbose_name='Trending Games old price')),
                ('new_price', models.PositiveIntegerField(verbose_name='Trending Games')),
                ('about', models.TextField(verbose_name='About game')),
                ('tags', models.CharField(max_length=50, verbose_name='TrendingGames tags')),
                ('reviews', models.TextField(verbose_name='TG Reviews')),
            ],
        ),
        migrations.AddField(
            model_name='trendinggames',
            name='reviews',
            field=models.TextField(default=1, verbose_name='TG Reviews'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trendinggames',
            name='tags',
            field=models.CharField(default=1, max_length=50, verbose_name='TrendingGames tags'),
            preserve_default=False,
        ),
    ]