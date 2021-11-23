from hotel.models import Room
from .availability import check_availability


def getAvailableRooms(category, check_in, check_out):
    # function that takes category and returns room list
    # Get queryset of rooms that satisfy the category
    room_list = Room.objects.filter(category=category)

    # Initialize Empty rooms
    available_rooms = []
    # populate the list
    for room in room_list:
        if check_availability(room, check_in, check_out):
            available_rooms.append(room)

    # check list of rooms
    if len(available_rooms) > 0:
        return available_rooms[0]
    else:
        return None
