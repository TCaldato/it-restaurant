from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_reservation, name='view_reservation'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path(
        'edit_booking/<int:booking_id>/',
        views.edit_booking, name='edit_booking'),
    path(
        'cancel_booking/<int:booking_id>/',
        views.cancel_booking, name='cancel_booking'),
]