from django import forms

from api.models import Parking, ParkingDetail


class CreateParkingForm(forms.ModelForm):

    class Meta:
        model = Parking
        fields = ['name']


class CreateParkingDetailForm(forms.ModelForm):

    class Meta:
        model = ParkingDetail
        fields = ['parking', 'arrival', 'departure']


class UpdateParkingDetailForm(forms.ModelForm):

    class Meta:
        model = ParkingDetail
        fields = ['arrival', 'departure']
