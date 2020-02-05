from django.contrib import admin
from .models import Room, Player

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'last_modified')

class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'created_at', 'last_modified')

admin.site.register(Room, RoomAdmin)
admin.site.register(Player, PlayerAdmin)