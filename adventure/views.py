from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RoomSerializer, PlayerSerializer
from .models import Room, Player



class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class PlayerView(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    # queryset = Player.objects.none()
    queryset = Player.objects.all()

    # def get_queryset(self):
    #     # line directly below is DEBUGGING
    #     # import pdb; pdb.set_trace()
    #     logged_in_user = self.request.user
    #     if logged_in_user.is_anonymous:
    #         return Player.objects.none()
    #     else:
    #         return Player.objects.filter(user=logged_in_user).order_by('created_at')
