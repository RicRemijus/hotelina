from django.db import models
from django.shortcuts import render, redirect, HttpResponse
from hotel.booking_functions.availability import check_availability
from django.urls import reverse_lazy, reverse
from hotel.forms import AvailableForm
from .models import Room, Booking
from django.views.generic import ListView, FormView, View, DeleteView
from hotel.booking_functions.get_room_cat_url_list import get_room_cat_url_list
from hotel.booking_functions.get_human_format_room_category import get_human_format_room_category
from hotel.booking_functions .get_available_rooms import getAvailableRooms
from hotel.booking_functions.book_room import book_room
# Create your views here.


def RoomListView(request):
    room_category_url_list = get_room_cat_url_list()

    context = {
        'room_list': room_category_url_list,
    }
    return render(request, 'hotel/room_list.html', context)


class BookingListView(ListView):
    model = Booking
    template_name = 'hotel/booking_list.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class RoomDetailView(View):
    # Genereic VIEW based RoomDetailView
    def get(self, request, *args, **kwargs):
        # Get room category from Kwargs
        category = self.kwargs.get('category', None)
        # get human readable formats
        human_format_room_category = get_human_format_room_category
        # Initialize empty form
        form = AvailableForm()
        room_list = Room.objects.filter(category=category)

        # check for invalid category Name
        if human_format_room_category is not None:
            context = {
                'room_category': human_format_room_category,
                'form': form,
            }
            return render(request, 'hotel/room_detail.html', context)
        else:
            return HttpResponse("Category doesnt exist")

    def post(self, request, *args, **kwargs):
        # Get Room category from keyword argument
        category = self.kwargs.get('category', None)
        # Pass Request.Post into AvailableFORM
        form = AvailableForm(request.POST)
        # checking form validity
        if form.is_valid():
            data = form.cleaned_data
        # Get available rooms
        available_rooms = getAvailableRooms(
            category, data['check_in'], data['check_out'], data['amount'])
        # Check if room are available
        if available_rooms is not None:
            # Book a room (First available room)
            booking = book_room(
                request, available_rooms[0], data['check_in'], data['check_out'])
            return HttpResponse(booking)
        else:
            return HttpResponse('all rooms are booked!')


class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'hotel/booking_confirm_delete.html'
    success_url = reverse_lazy('hotel:BookingListView')
