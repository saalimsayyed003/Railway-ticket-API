from django.shortcuts import render
from ticket.models import Reservation
from rest_framework import generics
from ticket.serializers import ReservationSerializers

class BookingList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation
    serializer_class = ReservationSerializers



