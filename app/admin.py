from django.contrib.admin import (
    ModelAdmin,
    display,
    register,
    site,
)

from app.models import (
    Category,
    District,
    Enterprise,
    NetworkEnterprise,
    Product,
    ProductPrice,
)

site.register(District)
site.register(Category)
site.register(NetworkEnterprise)
site.register(Product)


@register(Enterprise)
class EnterpriseAdmin(ModelAdmin):
    list_display = ("name", "network")
    list_filter = list_display + ("product",)


@register(ProductPrice)
class ProductPriceAdmin(ModelAdmin):
    list_display = ("product", "category", "price",)
    search_fields = ("get_product",)

    @display(description="Категория")
    def category(self, obj):
        return obj.product.category.name
