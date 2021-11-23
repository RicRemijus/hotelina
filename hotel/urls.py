from django.urls import path
from .views import BookingListView, RoomListView, RoomDetailView, CancelBookingView

app_name = 'hotel'

urlpatterns = [
    path('', RoomListView, name='roomList'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    #path('book/', BookingView.as_view(), name='booking_view'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(),
         name='CancelBookingView')
]
