from __future__ import unicode_literals

from django.db import models

from core import models as core_models

class Concept(core_models.Base):
	pass

class Relationship(core_models.Base):
	pass

class Related(core_models.Base):
	obj = models.ForeignKey(Concept, related_name="related_to")
	related_to = models.ForeignKey(Concept, related_name="related_from")
	relationship = models.ForeignKey(Relationship)

class Exercise(core_models.Base):
	pass
