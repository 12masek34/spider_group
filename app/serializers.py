from rest_framework.serializers import (
    ModelSerializer,
)

from app.models import (
    Category,
    District,
    Enterprise,
    NetworkEnterprise,
    Product,
    ProductPrice,
)


class NetworkEnterpriseSerializer(ModelSerializer):

    class Meta:
        model = NetworkEnterprise
        fields = "__all__"


class DistrictSerializer(ModelSerializer):

    class Meta:
        model = District
        fields = "__all__"


class ProductPriceSerializer(ModelSerializer):

    class Meta:
        model = ProductPrice
        fields = ("id", "price")


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    prices = ProductPriceSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class OrganizationSerializer(ModelSerializer):
    network = NetworkEnterpriseSerializer()
    district = DistrictSerializer(many=True)
    product = ProductSerializer(many=True)

    class Meta:
        model = Enterprise
        fields = "__all__"
