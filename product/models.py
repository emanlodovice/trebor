from __future__ import unicode_literals

from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, related_name='products')
    description = models.TextField()
    youtube_embed_url = models.URLField(blank=True)
    image_url = models.URLField()
    price = models.FloatField(null=True, blank=True)
    specs = models.TextField(blank=True)

    def __str__(self):
        return self.name
