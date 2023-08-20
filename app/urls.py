from django.urls import (
    path,
)
from rest_framework.routers import (
    DefaultRouter,
)

from app.views import (
    OrganizationByDistrictViewSet,
    OrganizationDetailAPIView,
    ProductViewSet,
)


router = DefaultRouter()
router.register(
     r"organizations/(?P<district_id>\d+)",
    OrganizationByDistrictViewSet,
    basename='organizations'
)
router.register('products', ProductViewSet, basename="products")

urlpatterns = [
    path("organization/<int:organization_id>", OrganizationDetailAPIView.as_view()),
]

urlpatterns += router.urls
