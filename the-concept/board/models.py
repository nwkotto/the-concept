from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes import fields, models as contenttype_models

from core import models as core_models

class Board(core_models.Base):
	pass

class Tile(core_models.Base):
	board = models.ForeignKey(Board)
	x = models.IntegerField()
	y = models.IntegerField()

	# Establish a foreign key to any piece of content
	content_type = models.ForeignKey(contenttype_models.ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content = fields.GenericForeignKey('content_type', 'object_id')