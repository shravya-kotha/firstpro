from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=30)
    slug = models. SlugField(max_length=30)