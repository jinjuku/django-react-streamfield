from django.contrib.admin.widgets import AutocompleteMixin
from django.forms import widgets


class AdminAutoHeightTextInput(widgets.Textarea):
    template_name = "django_react_streamfield/widgets/auto_height_text_input.html"

    def __init__(self, attrs=None):
        # Use more appropriate rows default, given autoheight will alter this anyway
        default_attrs = {"rows": "1"}
        if attrs:
            default_attrs.update(attrs)
            super().__init__(default_attrs)


class AdminAutocompleteChooser(AutocompleteMixin, widgets.HiddenInput):
    template_name = "django_react_streamfield/widgets/autocomplete_chooser.html"


class AdminAutocompleteMultipleChooser(AutocompleteMixin, widgets.HiddenInput):
    template_name = (
        "django_react_streamfield/widgets/autocomplete_multiple_chooser.html"
    )
