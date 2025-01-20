from room import Room
from character import Enemy

kitchen = Room("kitchen")
kitchen.set_description("a dank and dirty room buzzing with flies")

ballroom = Room("ballroom")
ballroom.set_description("a vast room with a shining wooden floor")

dining_hall = Room("dining hall")
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
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            print("what will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("you won the fight")
                current_room.set_character(None)
            else:
                print("you lost the fight")
                break
        else:
            print("there is no one here to fight with")