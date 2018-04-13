from django.contrib.postgres.fields import JSONField
from django.db import models
from foreignform.models import ForeignFormBaseModel


class TemplateModel(ForeignFormBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class InstanceModel(models.Model):
    template_model = models.ForeignKey(TemplateModel, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    form_data = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
