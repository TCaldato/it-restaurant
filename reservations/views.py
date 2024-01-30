from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking
from .forms import ReservationForm
from datetime import datetime
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate
from django.core.exceptions import ValidationError

# The number of appointments that can be taken
num_appointments = 1

def view_reservation(request):
    """
    Renders a view displaying upcoming bookings from the current date.
    """
    today_date = datetime.now()
    bookings = Booking.objects.filter(date__gte=today_date)
    context = {"bookings": bookings}
    return render(request, "reservations/views_reservation.html", context)

 
@login_required()
def create_booking(request):
    """
    View to handle the creation of a new booking
    """
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            chosen_date = form.cleaned_data["date"]
            chosen_time = form.cleaned_data["start_time"]
            num_people = form.cleaned_data["num_people"]

            # Check if the user has already booked for the chosen date
            existing_booking = Booking.objects.filter(
                user=request.user,
                date=chosen_date,
            ).first()

            if existing_booking:
                messages.error(request, "You have already booked for this date.")
                return redirect("create_booking")

            # Check if the total number of people booked for the chosen time exceeds the limit
            total_people_booked = Booking.objects.filter(
                date=chosen_date, start_time=chosen_time
            ).aggregate(total_people=Sum("num_people"))["total_people"]

            if total_people_booked is None:
                total_people_booked = 0

            if total_people_booked + num_people > 15:
                messages.error(
                    request,
                    f"No Booking available for {chosen_date} at {chosen_time}. Please choose another time.",
                )
                return redirect("create_booking")

            # Continue with the booking creation if the limit is not exceeded
            form.instance.user = request.user
            form.save()
            messages.success(
                request,
                f"Your appointment for {request.user.username} has been confirmed.",
            )
            return redirect("reservations")
    else:
        form = ReservationForm()

    context = {"form": form}
    return render(request, "reservations/create_booking.html", context)


@login_required()
def edit_booking(request, booking_id):
    """
    Handles the editing of an existing booking for the logged-in user or superuser.
    """

    # Get the existing booking or return a 404 if not found
    booking = get_object_or_404(Booking, id=booking_id)

    if not (request.user == booking.user or request.user.is_superuser):
        # If the user is neither the owner of the booking nor a superuser, deny access
        messages.error(request, "You don't have permission to edit this booking.")
        return redirect("reservations")

    if request.method == "POST":
        # If the request method is POST, process the form data
        form = ReservationForm(request.POST, instance=booking)
        if form.is_valid():
            # Extract relevant data from the form
            chosen_date = form.cleaned_data["date"]
            chosen_time = form.cleaned_data["start_time"]
            num_people = form.cleaned_data["num_people"]

            # Check if the total number of people booked for the chosen time exceeds the limit
            total_people_booked = Booking.objects.filter(
                date=chosen_date, start_time=chosen_time
            ).exclude(id=booking_id).aggregate(total_people=Sum("num_people"))["total_people"]

            if total_people_booked is None:
                total_people_booked = 0

            if total_people_booked + num_people > 15:
                messages.error(
                    request,
                    f"No Booking available for {chosen_date} at {chosen_time}. Please choose another time.",
                )
                return redirect("edit_booking", booking_id)
            
            # Check if there are conflicting bookings for the same date and time
            num_same_bookings = (
                Booking.objects.filter(
                    date=chosen_date, start_time=chosen_time
                )
                .exclude(id=booking_id)
                .count()
            )

            if num_same_bookings >= num_appointments:
                # If there are too many conflicting bookings, display an error message
                messages.error(
                    request, "No appointment available or this is your reservation"
                )
                return redirect("edit_booking", booking_id)
            else:
                # Save the form if there are no conflicts
                form.save()
                messages.success(
                    request,
                    f"The appointment has been changed successfully.",
                )
                return redirect("reservations")
    else:
        # If the request method is not POST, initialize the form with existing booking data
        form = ReservationForm(instance=booking)

    # Prepare the context for rendering the template
    context = {"form": form}
    return render(request, "reservations/edit_booking.html", context)


@login_required()
def cancel_booking(request, booking_id):
    """
    Handles the cancellation of an existing booking for the logged-in user.
    """

    # Get the existing booking or return a 404 if not found
    booking = get_object_or_404(Booking, id=booking_id)

    # Delete the booking and display a warning message
    booking.delete()
    messages.warning(request, "Your booking has been deleted")
    return redirect("reservations")
