#“How much building materials are needed to cover the entire floor #
# as well as how much baseboard we should have that will be installed into the room”

#all measurements are in ft
length_of_room=18
width_of_room= 14
door_length= 3

floor_material=length_of_room*width_of_room
baseboard= (2*length_of_room-door_length)+2*width_of_room

print(floor_material)
print(baseboard)