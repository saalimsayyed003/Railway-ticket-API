from rest_framework import serializers
from ticket.models import Reservation

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['From', 'To', 'Departure_date','Time']
