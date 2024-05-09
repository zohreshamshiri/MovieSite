# Generated by Django 5.0.3 on 2024-04-13 05:41

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('comment_text', models.CharField(blank=True, default='', max_length=600, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_title', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('picture', models.ImageField(upload_to='upload/news')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('query', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_title', models.CharField(blank=True, max_length=250, null=True)),
                ('director', models.CharField(blank=True, max_length=250, null=True)),
                ('casts', models.CharField(blank=True, max_length=250, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('release_year', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('download_link', models.CharField(blank=True, max_length=250, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('picture', models.ImageField(upload_to='upload/movie')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film2serial.category')),
                ('comments', models.ManyToManyField(to='film2serial.comment')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film2serial.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_title', models.CharField(blank=True, max_length=250, null=True)),
                ('director', models.CharField(blank=True, max_length=250, null=True)),
                ('casts', models.CharField(blank=True, max_length=250, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('release_year', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('download_link', models.CharField(blank=True, max_length=250, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('picture', models.ImageField(upload_to='upload/movie')),
                ('seasons', models.IntegerField()),
                ('episodes', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film2serial.category')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film2serial.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film2serial.category')),
                ('movies', models.ManyToManyField(to='film2serial.movie')),
                ('serials', models.ManyToManyField(to='film2serial.serial')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('biography', models.TextField()),
                ('movie_acted_in', models.ManyToManyField(to='film2serial.movie')),
                ('serial_acted_in', models.ManyToManyField(to='film2serial.serial')),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2024, 4, 13, 9, 11, 52, 800036))),
                ('movies', models.ManyToManyField(to='film2serial.movie')),
                ('serials', models.ManyToManyField(to='film2serial.serial')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film2serial.user')),
            ],
        ),
    ]
