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

    def specs_list(self):
        specs = self.specs.strip()
        specs_list = []
        if len(specs) > 0:
            specs = specs.split(',')
            for spec in specs:
                s = spec.strip()
                specs_list.append(s.split(':'))
        return specs_list

    @property
    def cost(self):
        return '%.2f' % self.price

    def __str__(self):
        return self.name
