from datetime import datetime

from rest_framework import serializers

from api.models import Parking, ParkingDetail


class ParkingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parking
        fields = '__all__'


class ParkingDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingDetail
        fields = '__all__'

    def validate(self, data):

        if data.get('arrival').timestamp() < datetime.today().timestamp():
            raise serializers.ValidationError(
                'arrival datetime cannot be less than the current datetime')

        if data.get('arrival').timestamp() >= data.get('departure').timestamp():
            raise serializers.ValidationError(
                'departure datetime cannot be less than the or equal to arrival datetime')

        return data
