from django.db import models
from django.contrib.postgres.fields import JSONField


class UserPercent(models.Model):
    user_id = models.BigIntegerField()
    courses = JSONField(default={})

