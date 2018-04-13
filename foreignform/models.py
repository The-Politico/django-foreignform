from django.contrib.postgres.fields import JSONField as PGJSONField
from django.db import models

from .fields import JSONField


class ForeignFormModel(models.Model):
    jsonSchema = JSONField()
    uiSchema = JSONField(null=True, blank=True)

    class Meta:
        abstract = True


class TemplateModel(ForeignFormModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class InstanceModel(models.Model):
    template_model = models.ForeignKey(TemplateModel, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    form_data = PGJSONField(blank=True, null=True)

    def __str__(self):
        return self.name
