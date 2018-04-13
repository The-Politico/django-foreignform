from django.contrib.admin import widgets as admin_widgets
from django.contrib.postgres.fields import JSONField

from .widgets import CodeMirrorWidget


class JSONField(JSONField):
    def __init__(self, *args, **kwargs):
        self.widget = CodeMirrorWidget()
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)

        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = self.widget
        return super().formfield(**defaults)
