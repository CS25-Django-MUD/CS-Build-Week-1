from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance",
              description="North of you, the cave mount beckons", x=0, y=0)

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""", x=0, y=1)

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")


r_test1 = Room(title="T1",
              description="North of you, the cave mount beckons")

r_test2 = Room(title="T2", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_test3 = Room(title="T3", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_test4 = Room(title="T4", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_test5 = Room(title="T5", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_test1.save()
r_test2.save()
r_test3.save()
r_test4.save()
r_test5.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")
r_test1.connectRooms(r_outside, "w")
r_outside.connectRooms(r_test1, "e")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_test1.connectRooms(r_test2, "s")
r_test2.connectRooms(r_test1, "n")

r_test2.connectRooms(r_test3, "e")  
r_test3.connectRooms(r_test2, "w")  

r_test3.connectRooms(r_test4, "s")
r_test4.connectRooms(r_test3, "n")

r_test4.connectRooms(r_test5, "e")
r_test5.connectRooms(r_test4, "w")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

# heroku command:  cat util/create_world.py | python manage.py shell
