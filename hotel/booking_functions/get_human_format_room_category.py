from hotel.models import Room


def get_human_format_room_category(category):
    '''
    A function that takes computer format room category and returns a human format room category
    '''
    room = Room.objects.all()[0]
    room_category = dict(room.ROOM_CATEGORY).get(category, None)
    return room_category
