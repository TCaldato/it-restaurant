from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
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
    return render(request, 'reservations/view_reservation.html', context)


@login_required()
def create_booking(request):
    """
    Create Booking:
    Handles the creation of a new booking for the logged-in user.
    """
    user = get_object_or_404(User, username=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            chosen_date = form.cleaned_data['date']
            chosen_time = form.cleaned_data['start_time']
            user_name = form.cleaned_data['user']
            num_same_bookings = Booking.objects.filter(
                date=chosen_date, start_time=chosen_time).count()

            if num_same_bookings >= num_appointments:
                messages.error(
                    request, f'No appointment available on {chosen_date} at {chosen_time}.')
                return redirect('create_booking')
            else:
                form.instance.user = user
                form.save()
                messages.success(
                    request, f'Your appointment for {user_name} has been confirmed.')
                return redirect('view_reservation')
    else:
        form = BookingForm()

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
    user = get_object_or_404(User, username=request.user)
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            chosen_date = form.cleaned_data['date']
            chosen_time = form.cleaned_data['start_time']
            user_name = form.cleaned_data['user']
            num_same_bookings = Booking.objects.filter(
                date=chosen_date, start_time=chosen_time).exclude(id=booking_id).count()

            if num_same_bookings >= num_appointments:
                messages.warning(
                    request, 'No appointment available or this is your reservation')
                return redirect('edit_booking', booking_id)
            else:
                form.save()
                messages.success(request, f'Your appointment for {user_name} has been changed.')
                return redirect('view_reservation')
    else:
        form = BookingForm(instance=booking)

    context = {
        'form': form
    }
    return render(request, 'reservations/edit_booking.html', context)


@login_required()
def cancel_reservation(request, booking_id):
    """
    Cancel reservation:
    Handles the cancellation of an existing booking for the logged-in user.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('view_reservation')