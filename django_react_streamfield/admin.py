from functools import update_wrapper

from django.contrib.admin.options import ModelAdmin
from django.urls import path

from .views import AutocompleteReverseLookupView


class StreamFieldAdmin(ModelAdmin):
    def get_urls(self):
        urlpatterns = super().get_urls()

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.model_name

        reverse_lookup = path(
            "autocomplete-reverse/",
            wrap(self.autocomplete_reverse_view),
            name="%s_%s_autocomplete_reverse" % info,
        )
        urlpatterns.insert(0, reverse_lookup)

        return urlpatterns

    def autocomplete_reverse_view(self, request):
        return AutocompleteReverseLookupView.as_view(model_admin=self)(request)
