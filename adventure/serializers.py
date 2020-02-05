from rest_framework import serializers
from .models import Room, Player

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'title', 'description', 'n_to', 's_to', 'e_to', 'w_to', 'created_at', 'last_modified')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('user', 'uuid', 'currentRoom', 'created_at', 'last_modified')