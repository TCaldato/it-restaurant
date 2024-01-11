import datetime
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    """
    Represents a booking for a user at a specific date and time.
    """

    class AppointmentTime(datetime.time, models.Choices):
        """
        Subclass appointment times for start_time field
        """
        PM_1800 = 18, 0, 0, '18:00'
        PM_1830 = 18, 30, 0, '18:30'
        PM_1900 = 19, 0, 0, '19:00'
        PM_1930 = 19, 30, 0, '19:30'
        PM_2000 = 20, 0, 0, '20:00'
        PM_2030 = 20, 30, 0, '20:30'
        PM_2100 = 21, 0, 0, '21:00'
        PM_2130 = 21, 30, 0, '21:30'
        

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(
        choices=AppointmentTime.choices, null=False,
        blank=False, default=AppointmentTime.PM_1800)
    

    class Meta:
        """Order bookings by time
        """
        ordering = ['date', 'start_time']

    def __str__(self):
        return str(self.user)