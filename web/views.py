from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from api.models import Parking, ParkingDetail
from web import forms
from web.permissions import ManagerPermissionMixin, EmployeeManagerPermissionMixin, SuperuserPermissionsMixin


class MainView(TemplateView):
    template_name = 'api/index.html'


class ParkingView(ListView):
    model = Parking
    template_name = 'api/parking.html'


class CreateParkingView(LoginRequiredMixin, SuperuserPermissionsMixin, CreateView):
    template_name = 'api/create_parking.html'
    form_class = forms.CreateParkingForm
    success_url = reverse_lazy('parking_places')


class DeleteParkingView(LoginRequiredMixin, SuperuserPermissionsMixin, DeleteView):
    model = Parking
    success_url = reverse_lazy('parking_places')


class ParkingDetailView(ListView):
    template_name = 'api/parking_detail.html'

    def get_queryset(self):
        new_context = ParkingDetail.objects.filter(parking=self.kwargs.get('pk'))

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parking = get_object_or_404(Parking, pk=self.kwargs.get('pk'))
        context['parking'] = parking

        return context


class CreateParkingDetailView(LoginRequiredMixin, EmployeeManagerPermissionMixin, CreateView):
    template_name = 'api/create_parking_detail.html'
    form_class = forms.CreateParkingDetailForm
    success_url = reverse_lazy('parking_places')


class DeleteParkingDetailView(LoginRequiredMixin, ManagerPermissionMixin, DeleteView):
    model = ParkingDetail
    success_url = reverse_lazy('parking_places')


class UpdateParkingDetailView(LoginRequiredMixin, ManagerPermissionMixin, UpdateView):
    model = ParkingDetail
    form_class = forms.UpdateParkingDetailForm
    success_url = reverse_lazy('parking_places')
    template_name = 'api/update_parking_detail.html'
