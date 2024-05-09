from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.User)
admin.site.register(models.News)
admin.site.register(models.Movie)
admin.site.register(models.Serial)
admin.site.register(models.Comment)
admin.site.register(models.Actor)
admin.site.register(models.Category1)
admin.site.register(models.Genre)
admin.site.register(models.Search)
admin.site.register(models.Watchlist)