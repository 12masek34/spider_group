from django.db.models import (
    QuerySet,
)
from django.shortcuts import (
    get_object_or_404,
)
from django_filters.rest_framework import (
    DjangoFilterBackend,
)
from rest_framework.filters import (
    SearchFilter,
)
from rest_framework.generics import (
    RetrieveAPIView,
)
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.viewsets import (
    GenericViewSet,
    ModelViewSet,
)

from app.models import (
    District,
    Enterprise,
    Product,
)
from app.serializers import (
    OrganizationSerializer,
    ProductCreateSerializer,
)


class OrganizationByDistrictViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """Список заведений - с условием заранее выбранного района.

    Возможно выполнить фильтрацию по названию категори.
    Возможно выполнить поиск по имени товара.

    Пример запроса -
        curl --location 'http://127.0.0.1:8000/api/organizations/1/' \
        --header 'Authorization: Token 990d9608a0bd71c2d099ba121688a6194b4046a1'

    Пример запроса с фильтром по категории -
        curl --location 'http://127.0.0.1:8000/api/organizations/3/?product__category__name=category_name' \
        --header 'Authorization: Token 990d9608a0bd71c2d099ba121688a6194b4046a1'

    Пример запроса с фильтром для поиска по имени продукта -
        curl --location 'http://127.0.0.1:8000/api/organizations/3/?search=product_name' \
        --header 'Authorization: Token 990d9608a0bd71c2d099ba121688a6194b4046a1'
    """
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ("get",)
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ("product__category__name",)
    search_fields = ("product__name",)

    def get_queryset(self) -> QuerySet:
        district = get_object_or_404(District, id=self.kwargs.get("district_id"))

        return district.enterprises.all()


class OrganizationDetailAPIView(RetrieveAPIView):
    """Детальная информация по заведению.

    Пример запроса -
        curl --location 'http://127.0.0.1:8000/api/organization/1' \
        --header 'Authorization: Token 990d9608a0bd71c2d099ba121688a6194b4046a1'
    """
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Enterprise.objects.all()
    lookup_url_kwarg = "organization_id"


class ProductViewSet(ModelViewSet):
    """Добавление товара/услуги и детальная информация по товару/услуге.

    Пример запроса добавления -
        curl --location 'http://127.0.0.1:8000/api/products/' \
        --header 'Authorization: Token 990d9608a0bd71c2d099ba121688a6194b4046a1' \
        --header 'Content-Type: application/json' \
        --data '{
            "category": {
                "name": "name"
            },
            "name": "name"
        }
        '
    Пример запроса детальной информации -
        curl --location 'http://127.0.0.1:8000/api/products/1' \
        --header 'Authorization: Token 990d9608a0bd71c2d099ba121688a6194b4046a1'
    """
    serializer_class = ProductCreateSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    http_method_names = ("post", "get")
