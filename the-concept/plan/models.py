from __future__ import unicode_literals

from django.db import models

from core import models as core_models
from concept import models as concept_models

class Plan(core_models.Base):
	pass

class Milestone(core_models.Base):
	pass

class Commitment(core_models.Base):
	plan = models.ForeignKey(Plan)
	exercise = models.ForeignKey(concept_models.Exercise)
	start = models.DateField()
	end = models.DateField(null=True, blank=True)

class CommitmentMilestone(core_models.Base):
	commitment = models.ForeignKey(Commitment)
	milestone = models.ForeignKey(Milestone)
	date = models.DateField()