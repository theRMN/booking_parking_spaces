from django import forms
from django.core.exceptions import ValidationError

from datetime import datetime

from api.models import Parking, ParkingDetail


class CreateParkingForm(forms.ModelForm):

    class Meta:
        model = Parking
        fields = ['name']


class CreateParkingDetailForm(forms.ModelForm):

    class Meta:
        model = ParkingDetail
        fields = ['parking', 'arrival', 'departure']

    def clean(self):
        arrival = self.cleaned_data['arrival']
        departure = self.cleaned_data['departure']

        if arrival.timestamp() < datetime.today().timestamp():
            raise ValidationError('arrival datetime cannot be less than the current datetime')

        if arrival.timestamp() >= departure.timestamp():
            raise ValidationError('departure datetime cannot be less than the or equal to arrival datetime')

        return self.cleaned_data


class UpdateParkingDetailForm(CreateParkingDetailForm):

    class Meta:
        model = ParkingDetail
        fields = ['arrival', 'departure']
