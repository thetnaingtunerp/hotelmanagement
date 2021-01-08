from django.shortcuts import render,HttpResponse
from django.views.generic import ListView, FormView
import datetime
from .models import *
from .forms import *
# Create your views here.
def check_availability(room, check_in, check_out):
    avail_list =[]
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)


class RoomList(ListView):
    model = Room

class BookingList(ListView):
    model = Booking

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_room =[]
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_room.append(room)
        if len(available_room)>0:
            room = available_room[0]
            booking = Booking.objects.create(user=self.request.user,room=room, check_in= data['check_in'], check_out=data['check_out'])
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('This Room is Booked')