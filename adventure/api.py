from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    roomid = room.id
    players = room.playerNames(player_id)
    return JsonResponse({'roomid': roomid,'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    print("player: ", player)
    player_id = player.id
    print("player_id: ", player_id)
    player_uuid = player.uuid
    print("uuid: ", player_uuid)
    data = json.loads(request.body)
    print("data: ", data)
    direction = data['direction']
    print("direction: ", direction)
    room = player.room()
    print("room: ", room)
    nextRoomID = None
    print("nextRoomID: ", nextRoomID)
    if direction == "n":
        nextRoomID = room.n_to
        print("nextRoomID, post n: ", nextRoomID)
    elif direction == "s":
        nextRoomID = room.s_to
        print("nextRoomID, post s: ", nextRoomID)
    elif direction == "e":
        nextRoomID = room.e_to
        print("nextRoomID, post e: ", nextRoomID)
    elif direction == "w":
        nextRoomID = room.w_to
        print("nextRoomID, post w: ", nextRoomID)
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        print("nextRoom: ", nextRoom)
        player.currentRoom=nextRoomID
        print("player.currentRoom: ", player.currentRoom)
        player.save()
        players = nextRoom.playerNames(player_id)
        print("players:  ", players)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        print("currentPlayerUUIDS: ", currentPlayerUUIDs)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        print("nextPlayerUUIDs: ", nextPlayerUUIDs)
        # for p_uuid in currentPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        # for p_uuid in nextPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        print("A WHOLE LOTTA $(*($*)):  ", JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True))
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        print("ALL THE WRONG #$*()&$@)(!!):  ", JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True))
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)
