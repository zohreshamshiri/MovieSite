from django.db import models

import datetime


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class User(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user_name} {self.email}'


class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    comment_text = models.CharField(max_length=600, default='', null=True, blank=True)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    original_title = models.CharField(max_length=250, null=True, blank=True)
    director = models.CharField(max_length=250, null=True, blank=True)
    casts = models.CharField(max_length=250, null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=600, default='', null=True, blank=True)
    rating = models.DecimalField(default=0, decimal_places=1, max_digits=3)
    download_link = models.CharField(max_length=250, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='upload/movie')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.original_title


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    original_title = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=600, default='', null=True, blank=True)
    picture = models.ImageField(upload_to='upload/news')

    def __str__(self):
        return self.original_title


class Search(models.Model):
    id = models.IntegerField(primary_key=True)
    query = models.CharField(max_length=250, null=True, blank=True)


class Serial(models.Model):
    id = models.IntegerField(primary_key=True)
    original_title = models.CharField(max_length=250, null=True, blank=True)
    director = models.CharField(max_length=250, null=True, blank=True)
    casts = models.CharField(max_length=250, null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=600, default='', null=True, blank=True)
    rating = models.DecimalField(default=0, decimal_places=1, max_digits=3)
    download_link = models.CharField(max_length=250, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='upload/movie')

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    seasons = models.IntegerField()
    episodes = models.IntegerField()

    def __str__(self):
        return self.original_title


class Actor(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField()
    movie_acted_in = models.ManyToManyField(Movie)
    serial_acted_in = models.ManyToManyField(Serial)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
    serials = models.ManyToManyField(Serial)
    date = models.DateField(default=datetime.datetime.today())


class Category1(models.Model):
    title = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    movies = models.ManyToManyField(Movie)
    serials = models.ManyToManyField(Serial)
