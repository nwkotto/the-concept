from django.contrib import admin

import models

admin.site.register([models.Concept, models.Relationship, models.Related, models.Exercise])
