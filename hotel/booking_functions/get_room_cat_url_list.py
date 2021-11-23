from django.urls.base import reverse_lazy
from hotel.models import Room
from django.urls import reverse_lazy, reverse

# Function that returns different room category and room url list


def get_room_cat_url_list():
    room = Room.objects.all()[0]  # Getting a random ROOM object
    # making a dictionary from ROOM_CATEGORY tupple on the ROOM
    room_categories = dict(room.ROOM_CATEGORY)
    room_cat_url_list = []  # Empty Room (category, url) list

    for category in room_categories:  # loop for populating the room_cat_url_list
        room_category = room_categories.get(category)
        room_url = reverse_lazy('hotel:RoomDetailView', kwargs={
                                'category': category})
        room_cat_url_list.append((room_category, room_url))
    return room_cat_url_list
