from django.contrib import admin

import models

admin.site.register([models.Plan, models.Milestone, models.Commitment, models.CommitmentMilestone])
