from hotel.models import Room, Booking


def check_availability(room, check_in, check_out):
    available_room_list = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            available_room_list.append(True)
        else:
            available_room_list.append(False)
    return all(available_room_list)
