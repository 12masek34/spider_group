from django.shortcuts import (
    get_object_or_404,
)
from django_filters.rest_framework import (
    DjangoFilterBackend,
)
from rest_framework.filters import (
    SearchFilter,
)
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.viewsets import (
    GenericViewSet,
)

from app.models import (
    District,
)
from app.serializers import (
    OrganizationSerializer,
)


class OrganizationByDistrictViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = OrganizationSerializer
    http_method_names = ("get",)
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ("product__category__name",)
    search_fields = ("product__name",)

    def get_queryset(self):
        district = get_object_or_404(District, id=self.kwargs.get("district_id"))

        return district.enterprises.all()
