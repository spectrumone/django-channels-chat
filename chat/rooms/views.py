from django.db import transaction
from django.shortcuts import render, redirect
import haikunator
from .models import Room, Message

from django.shortcuts import render

# Create your views here.
def about(request):
    if request.user.is_authenticated():
        profile = request.user.profile
        messages = Message.objects.filter(owner=profile)
        rooms = Room.objects.filter(pk__in=messages.values('pk')).distinct()

    return render(request, "chat/about.html", {'rooms': rooms})


def new_room(request):
    """
    Randomly create new room, and redirect to it.
    """
    new_room = None
    while not new_room:
        with transaction.atomic():
            label = haikunator.haikunate()
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label){}

    return redirect(chat_room, label=label)



def chat_room(request, label):
    """
    Room view - show the room, with latest messages.
    The template for this view has the WebSocket business to send and stream
    messages, so see the template for where the magic happens.
    """

    room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    if not request.user.is_authenticated():
        return redirect('about')

    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages
    })
