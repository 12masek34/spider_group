from rest_framework.routers import (
    DefaultRouter,
)

from app.views import (
    OrganizationByDistrictViewSet,
)


router = DefaultRouter()
router.register(
     r"organizations/(?P<district_id>\d+)",
    OrganizationByDistrictViewSet,
    basename='organizations'
)

urlpatterns = router.urls
