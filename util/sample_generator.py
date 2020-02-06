# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.

import sys
sys.path.append('../adventure')
from .adventure import Room as Room_m

# class Room:
#     def __init__(self, id, name, description, x, y):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.n_to = None
#         self.s_to = None
#         self.e_to = None
#         self.w_to = None
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         if self.e_to is not None:
#             return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
#         return f"({self.x}, {self.y})"
        
#     def connect_rooms(self, connecting_room, direction):
#         '''
#         Connect two rooms in the given n/s/e/w direction
#         '''
#         reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
#         reverse_dir = reverse_dirs[direction]
#         setattr(self, f"{direction}_to", connecting_room)
#         setattr(connecting_room, f"{reverse_dir}_to", self)
        
#     def get_room_in_direction(self, direction):
#         '''
#         Connect two rooms in the given n/s/e/w direction
#         '''
#         return getattr(self, f"{direction}_to")


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
    def generate_rooms(self, size_x, size_y, num_rooms):
        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x
        x = -5
        y = 0
        room_count = 0
        # Start generating rooms to the east
        direction = 1 #1:east, -1:west
        # While there are rooms to be created...
        previous_room = None
        room_titles = ["Outside Cave Entrance", "Foyer", "Grand Overlook", "Narrow Passage", "Treasure Chamber"]
        room_descriptions = ["North of you, the cave mount beckons", """Dim light filters in from the south. Dusty
        passages run north and east.""", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.""", """The narrow passage bends here from west
        to north. The smell of gold permeates the air.""", """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south."""]
        while room_count < num_rooms:
            if direction > 0 and x < size_x - 5:
                room_direction = "e"
                x += 5
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 5
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 5
                direction *= -1
            # Create a room in the given direction
            import random
            num = random.choice(range(0,5))
            room = Room_m(room_count, room_titles[num], room_descriptions[num], x, y)
            room.objects.save()
            self.grid[y][x] = room
            if previous_room is not None:
                previous_room.connect_rooms(room, room_direction)
            # Update iteration variables
            previous_room = room
            room_count += 1



    # def print_rooms(self):
    #     '''
    #     Print the rooms in room_grid in ascii characters.
    #     '''

    #     # Add top border
    #     str = "# " * ((3 + self.width * 5) // 2) + "\n"

    #     # The console prints top to bottom but our array is arranged
    #     # bottom to top.
    #     #
    #     # We reverse it so it draws in the right direction.
    #     reverse_grid = list(self.grid) # make a copy of the list
    #     reverse_grid.reverse()
    #     for row in reverse_grid:
    #         # PRINT NORTH CONNECTION ROW
    #         str += "#"
    #         for room in row:
    #             if room is not None and room.n_to is not None:
    #                 str += "  |  "
    #             else:
    #                 str += "     "
    #         str += "#\n"
    #         # PRINT ROOM ROW
    #         str += "#"
    #         for room in row:
    #             if room is not None and room.w_to is not None:
    #                 str += "-"
    #             else:
    #                 str += " "
    #             if room is not None:
    #                 str += f"{room.id}".zfill(3)
    #             else:
    #                 str += "   "
    #             if room is not None and room.e_to is not None:
    #                 str += "-"
    #             else:
    #                 str += " "
    #         str += "#\n"
    #         # PRINT SOUTH CONNECTION ROW
    #         str += "#"
    #         for room in row:
    #             if room is not None and room.s_to is not None:
    #                 str += "  |  "
    #             else:
    #                 str += "     "
    #         str += "#\n"

    #     # Add bottom border
    #     str += "# " * ((3 + self.width * 5) // 2) + "\n"

    #     # Print string
    #     print(str)


num_rooms = 100
width = 50
height = 50

# def create_world():
w = World()
w.generate_rooms(width, height, num_rooms)
    # w.print_rooms()
    # print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
    # return w
    
# create_world()

# heroku command:  cat util/sample_generator.py | python3 manage.py shell
