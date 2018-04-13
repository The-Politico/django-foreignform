import json


class ForeignFormAdminMixin(object):
    foreignform_field = None
    foreignform_foreign_key = None
    change_form_template = 'foreignform/change.html'
    add_form_template = 'foreignform/add.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        instance = self.model.objects.get(id=object_id)
        fk = getattr(instance, self.foreignform_foreign_key)

        extra_context = extra_context or {}
        extra_context['foreignform_field'] = self.foreignform_field
        extra_context['foreignform_JSONSchema'] = json.dumps(fk.jsonSchema)
        extra_context['foreignform_UISchema'] = json.dumps(fk.uiSchema)
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['foreignform_field'] = self.foreignform_field
        extra_context['foreignform_foreign_key'] = self.foreignform_foreign_key
        return super().add_view(
            request, form_url, extra_context=extra_context,
        )
