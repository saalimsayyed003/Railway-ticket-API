from django.urls import path,include
from ticket.views import BookingList,BookingDetail

urlpatterns = [
    path('api/bookings', BookingList.as_view()),
    path('api/bookings/<int:pk>',BookingDetail.as_view()),
    path('', include('ticket.urls')),

]

