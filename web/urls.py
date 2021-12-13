from django.urls import path

from web import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main_page'),
    path('parking_places/', views.ParkingView.as_view(), name='parking_places'),
    path('parking_places/<int:pk>/', views.ParkingDetailView.as_view()),
    path('create_parking/', views.CreateParkingView.as_view(), name='create_parking'),
    path('delete_parking/<int:pk>/', views.DeleteParkingView.as_view(), name='delete_parking'),
    path('create_parking_detail/', views.CreateParkingDetailView.as_view(), name='create_parking_detail'),
    path('delete_parking_detail/<int:pk>/', views.DeleteParkingDetailView.as_view(), name='delete_parking_detail'),
    path('update_parking_detail/<int:pk>/', views.UpdateParkingDetailView.as_view(), name='update_parking_detail')
]
