from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking
from .forms import ReservationForm
from datetime import datetime

# The number of appointments that can be taken
num_appointments = 1


def view_reservation(request):
    """
    View Reservation:
    Renders a view displaying upcoming bookings from the current date.
    """
    today_date = datetime.now()
    bookings = Booking.objects.filter(date__gte=today_date)
    context = {
        'bookings': bookings
    }
    return render(request, 'reservations/views_reservation.html', context)


@login_required()
def create_booking(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            chosen_date = form.cleaned_data['date']
            chosen_time = form.cleaned_data['start_time']
            num_people = form.cleaned_data['num_people']
            user_name = request.user.username
            num_same_bookings = Booking.objects.filter(
                date=chosen_date, start_time=chosen_time, user=request.user).count()

            if num_same_bookings >= num_appointments:
                messages.error(
                    request, f'No appointment available on {chosen_date} at {chosen_time}.')
                return redirect('create_booking')
            else:
                form.instance.user = request.user
                form.instance.num_people = num_people  # Set the number of people
                form.save()
                messages.success(
                    request, f'Your appointment for {user_name} has been confirmed.')
                return redirect('reservations')
    else:
        form = ReservationForm()

    context = {
        'form': form
    }
    return render(request, 'reservations/create_booking.html', context)


@login_required()
def edit_booking(request, booking_id):
    """
    Edit booking:
    Handles the editing of an existing booking for the logged-in user.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=booking)
        if form.is_valid():
            chosen_date = form.cleaned_data['date']
            chosen_time = form.cleaned_data['start_time']
            num_people = form.cleaned_data['num_people']
            num_same_bookings = Booking.objects.filter(
                date=chosen_date, start_time=chosen_time, user=request.user).exclude(id=booking_id).count()

            if num_same_bookings >= num_appointments:
                messages.warning(
                    request, 'No appointment available or this is your reservation')
                return redirect('edit_booking', booking_id)
            else:
                form.save()
                messages.success(request, f'Your appointment for {request.user.username} has been changed.')
                return redirect('reservations')
    else:
        form = ReservationForm(instance=booking)

    context = {
        'form': form
    }
    return render(request, 'reservations/edit_booking.html', context)


@login_required()
def cancel_booking(request, booking_id):
    """
    Cancel reservation:
    Handles the cancellation of an existing booking for the logged-in user.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.warning(request, 'Your booking has been deleted')
    return redirect('reservations')

