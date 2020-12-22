# Generated by Django 3.1.3 on 2020-11-29 15:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Актеры и режиссеры',
                'verbose_name_plural': 'Актеры и режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='категория')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.SlugField(max_length=150)),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Називание')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='описание')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='постер')),
                ('year', models.PositiveSmallIntegerField(default=2019, verbose_name='дата выхода')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('world_premiere', models.DateField(default=datetime.date.today)),
                ('budget', models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='бюджет')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='сбор в сша')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='черновик')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='Актеры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='режиссер')),
                ('genres', models.ManyToManyField(to='movies.Genre', verbose_name='жанры')),
            ],
            options={
                'verbose_name': 'фильм',
                'verbose_name_plural': 'фильмы',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'звезда рейтинга',
                'verbose_name_plural': 'звезда рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Собшение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Фильм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзив',
                'verbose_name_plural': 'Отзивы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.movie', verbose_name='фильм')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'рейтинг',
                'verbose_name_plural': 'рейтинги',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='изображение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='фильм')),
            ],
            options={
                'verbose_name': 'кадри из фильма',
                'verbose_name_plural': 'кадри из фильма',
            },
        ),
    ]