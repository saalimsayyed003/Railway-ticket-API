from django.db import models

class Reservation(models.Model):
    From = models.CharField(max_length=50, blank=True)
    To = models.CharField(max_length=50, blank=True)
    Departure_date = models.DateField(blank=True)
    Time = models.TimeField()



