from django.contrib import admin
from . import models

admin.site.register(models.ArticleCategory)
admin.site.register(models.Article)
