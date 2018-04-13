from django.contrib import admin
from foreignform.mixins import ForeignFormAdminMixin

from .models import InstanceModel, TemplateModel


class TemplateAdmin(admin.ModelAdmin):
    fields = ('name', 'jsonSchema', 'uiSchema',)


class InstanceAdmin(ForeignFormAdminMixin, admin.ModelAdmin):
    foreignform_field = 'form_data'
    foreignform_foreign_key = 'template_model'


admin.site.register(TemplateModel, TemplateAdmin)
admin.site.register(InstanceModel, InstanceAdmin)
