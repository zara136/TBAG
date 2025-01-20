from room import Room
from character import Enemy

kitchen = Room()
kitchen.set_name('kitchen')
kitchen.set_description("a dank and dirty room buzzing with flies")

ballroom = Room()
ballroom.set_name('ballroom')
ballroom.set_description("a vast room with a shining wooden floor")

dining_hall = Room()
dining_hall.set_name('dining hall')
dining_hall.set_description("a large room with ornate golden decorations")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

dave = Enemy("dave", "a smelly zombie")
dave.set_conversation("brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

current_room = kitchen
while True:
    print("\n")
    current_room.get_details()
    
    inhabitant = current_room.get_character()
    
    if inhabitant is not None:
        inhabitant.describe()
        command = input("> ")
        current_room = current_room.move(command)