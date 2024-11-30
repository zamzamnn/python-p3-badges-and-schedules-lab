# def badge_maker(name):
#     return None

# def batch_badge_creator(names):
#     return None

# def assign_rooms(names):
#     return None

# def printer(names):
#     return None

# badge_maker function: Returns a badge message for a single person
def badge_maker(name):
    return f"Hello, my name is {name}."

# batch_badge_creator function: Returns a list of badge messages for all names in the list
def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

# assign_rooms function: Assigns each person in the list to a room, with the room number based on the index
def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {i+1}!" for i, name in enumerate(names)]

# printer function: Prints both badge messages and room assignments for a list of names
def printer(names):
    # Generate badge messages
    badge_messages = batch_badge_creator(names)
    # Generate room assignments
    room_assignments = assign_rooms(names)
    
    # Print all badge messages
    for message in badge_messages:
        print(message)
    
    # Print all room assignments
    for assignment in room_assignments:
        print(assignment)
