from django.db import models
from django.conf import settings
# Create your models here.
class Room(models.Model):
    ROOM_CATEGORY = (
        ('AC','AC'),('NAC','NAC'),('KING','KING'),('QUEEN','QUEEN'),('DELUX','DELUX')
    )
    number = models.IntegerField()
    category = models.CharField(max_length=225, choices=ROOM_CATEGORY)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user}'