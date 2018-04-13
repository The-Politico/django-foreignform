from django.db import models

from .fields import JSONField


class ForeignFormBaseModel(models.Model):
    jsonSchema = JSONField(blank=True, null=True)
    uiSchema = JSONField(blank=True, null=True)

    class Meta:
        abstract = True
