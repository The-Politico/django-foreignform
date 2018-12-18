from django.forms import widgets
from django.utils.safestring import mark_safe


class CodeMirrorWidget(widgets.Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        if "class" not in attrs.keys():
            attrs["class"] = ""

        attrs["class"] += " codemirror-json-editor"

        html = super().render(name, value, attrs)

        return mark_safe(html)

    class Media:
        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.36.0/codemirror.min.js",  # noqa: E501
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.36.0/mode/javascript/javascript.min.js",  # noqa: E501
            "https://cdnjs.cloudflare.com/ajax/libs/jsonlint/1.6.0/jsonlint.min.js",  # noqa: E501
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.36.0/addon/lint/lint.min.js",  # noqa: E501
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.36.0/addon/lint/json-lint.min.js",  # noqa: E501
            "foreignform/js/codemirror.js",
        )

        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.36.0/codemirror.min.css",  # noqa: E501
                "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.36.0/theme/cobalt.min.css",  # noqa: E501
                "https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.36.0/addon/lint/lint.min.css",  # noqa: E501
                "foreignform/css/codemirror.css",
            )
        }
