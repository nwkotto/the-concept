from __future__ import unicode_literals
import datetime

from django.db import models

import autoslug

class Base(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    slug = autoslug.AutoSlugField(null=True, blank=True, populate_from="name")
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        super(Base, self).save(*args, **kwargs)

    class Meta:
        abstract = True