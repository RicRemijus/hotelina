from django.db import models
from django.conf import settings
from django.urls import reverse_lazy, reverse

# Create your models here.


class Room(models.Model):
    ROOM_CATEGORY = (
        ('AMB', 'AMBASSADORIAL SUIT'),
        ('EXE', 'EXECUTIVE ROOM'),
        ('STA', 'STANDARD ROOM'),
    )
    room_number = models.IntegerField()
    category = models.CharField(max_length=20, choices=ROOM_CATEGORY)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self) -> str:
        return f" {self.category} {self.room_number} with {self.beds} bed for {self.capacity} guests"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    booked_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return f" {self.user}  booked  {self.room}  from {self.check_in}  to   {self.check_out}"

    def get_room_category(self):
        room_categories = dict(self.room.ROOM_CATEGORY)
        room_category = room_categories.get(self.room.category)
        return room_category

    def get_cancel_booking_url(self):
        return reverse_lazy('hotel:CancelBookingView', args=[self.pk, ])
