from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from api import serializers
from api.models import ParkingDetail, Parking
from api.permissions import IsManagerPermissionOrIsAdminUser, IsEmployeePermissionOrIsAdminUser


class ParkingViewSet(ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = serializers.ParkingSerializer

    def get_permissions(self):

        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminUser()]

        return []


class ParkingDetailViewSet(ModelViewSet):
    queryset = ParkingDetail.objects.all()
    serializer_class = serializers.ParkingDetailSerializer

    def get_permissions(self):

        if self.action in ["create"]:
            return [IsAuthenticated(), IsEmployeePermissionOrIsAdminUser()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsManagerPermissionOrIsAdminUser()]

        return []
