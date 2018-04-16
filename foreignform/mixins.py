import json

from django.core.exceptions import FieldDoesNotExist


class ForeignFormAdminMixin(object):
    foreignform_field = None
    foreignform_foreign_key = None
    foreignform_jsonschema_field = 'jsonSchema'
    foreignform_uischema_field = 'uiSchema'
    change_form_template = 'foreignform/change.html'
    add_form_template = 'foreignform/add.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        instance = self.model.objects.get(id=object_id)
        fk = getattr(instance, self.foreignform_foreign_key, None)

        if not fk:
            raise FieldDoesNotExist(
                'Field "{}" does not exist on model. Check the '
                '"foreignform_foreign_key" attribute on your foreignform '
                'ModelAdmin class.'.format(
                    self.foreignform_foreign_key
                )
            )

        extra_context = extra_context or {}
        extra_context['foreignform_field'] = self.foreignform_field

        try:
            json_schema = getattr(fk, self.foreignform_jsonschema_field)
        except AttributeError as error:
            raise FieldDoesNotExist(
                'Field "{}" does not exist on foreign-keyed model, {}. Check '
                'the "foreignform_jsonschema_field" attribute on your '
                'foreignform ModelAdmin class.'.format(
                    self.foreignform_jsonschema_field,
                    self.foreignform_field,
                )
            )
        try:
            ui_schema = getattr(fk, self.foreignform_uischema_field)
        except AttributeError as error:
            raise FieldDoesNotExist(
                'Field "{}" does not exist on foreign-keyed model, {}. Check '
                'the "foreignform_uischema_field" attribute on your '
                'foreignform ModelAdmin class.'.format(
                    self.foreignform_uischema_field,
                    self.foreignform_field,
                )
            )
        extra_context['foreignform_JSONSchema'] = json.dumps(json_schema)
        extra_context['foreignform_UISchema'] = json.dumps(ui_schema)
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
