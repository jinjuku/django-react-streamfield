from django.http import JsonResponse
from django.views.generic.list import BaseListView


class AutocompleteReverseLookupView(BaseListView):
    """
    Provide reverse lookup for ChooserBlock.
    Based on: django/contrib/admin/views/autocomplete.py
    """

    model_admin = None

    def get(self, request, *args, **kwargs):
        """
        Return a JsonResponse with results of the form:
        {
            results: [{id: "123" text: "foo"}]
        }
        """
        self.preflight(request)
        ids = self.get_ids(request)
        queryset = self.get_queryset(ids)
        return JsonResponse(
            {"results": [{"id": str(obj.pk), "text": str(obj)} for obj in queryset]}
        )

    def preflight(self, request):
        if not self.has_perm(request):
            return JsonResponse({"error": "403 Forbidden"}, status=403)

    def get_ids(self, request):
        try:
            return [int(ID) for ID in request.GET.getlist("id")]
        except ValueError:
            return []

    def get_queryset(self, ids):
        """Return queryset based on ModelAdmin.get_search_results()."""
        qs = self.model_admin.get_queryset(self.request)
        if len(ids):
            return qs.filter(id__in=ids)
        else:
            return qs.model.objects.none()

    def has_perm(self, request, obj=None):
        """Check if user has permission to access the related model."""
        return self.model_admin.has_view_permission(request, obj=obj)
