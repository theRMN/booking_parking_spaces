from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('parking_details', views.ParkingDetailViewSet)
router.register('parking_places', views.ParkingViewSet)

urlpatterns = router.urls
