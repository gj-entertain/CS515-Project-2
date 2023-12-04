import json
import inspect
import sys


def load_map(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def create_world_state(game_map):
    world_state = {}
    for i, room in enumerate(game_map):
        world_state[i] = {'name': room['name'], 'desc': room['desc'], 'exits': room['exits'], 'items': room.get('items', [])}
    return world_state

def display_room(room):
    print(f"> {room['name']}\n")
    print(room['desc'])
    if room['items']:
        print("\nItems:", ", ".join(room['items']))
    print("\nExits:", " ".join(room['exits'].keys()))
    print()
    

def go(world_state, current_room, direction):
    exits = world_state[current_room]['exits']
    if direction not in exits:
        print(f"There's no way to go {direction}.")
        return current_room
    else:
        destination = exits[direction]
        print(f"You go {direction}.\n")
        display_room(world_state[destination])
        return destination

def look(world_state, current_room):
    display_room(world_state[current_room])


def get(world_state, current_room, inventory_items, item):
    items = world_state[current_room]['items']
    if item not in items:
        print(f"There's no {item} anywhere.")
    else:
        items.remove(item)
        inventory_items.append(item)
        print(f"You pick up the {item}.")
        return item

def drop(world_state, current_room, inventory_items, item):
    if item not in inventory_items:
        print(f"You don't have {item} in your inventory.")
    else:
        inventory_items.remove(item)
        world_state[current_room]['items'].append(item)
        print(f"You drop the {item}.")
        return item

def inventory(inventory_items):
    if inventory_items:
        print("Inventory:\n", ", ".join(inventory_items))
    else:
        print("You're not carrying anything.")

def quit_game():
    print("Goodbye!")
    quit()

def help():
    help_command()



def help_command():
    current_module = sys.modules[__name__]
    function_list = [o for o in inspect.getmembers(current_module) if inspect.isfunction(o[1])]
    filter_list = ['create_world_state', 'display_room', 'help_command', 'load_map', 'quit_game']

    # Print header line
    print("You can run the following commands:")

    for function in function_list:
        if function[0] in ['go', 'get']:
            print("  " + function[0] + ' ...')  # Indented command
        elif function[0] not in filter_list:
            print("  " + function[0])  # Indented command

    # Print 'quit' command at the end
    print("  quit")


if len(sys.argv) < 2:
    print("Please provide a filename ")
    sys.exit()

filename = sys.argv[1]

game_map = load_map(filename)
world_state = create_world_state(game_map)
current_room = 0
inventory_items = []
# change this max HP to test
HP = 1000
# Change the target magic_wind you need.
magic_wind = "rose"
display_room(world_state[current_room])
while True:
    try:
        action = input("What would you like to do? ")
        action = action.strip().lower().split()
        verb = action[0]
        if HP == 0:
            if not inventory_items.__contains__(magic_wind):
                print("You lose!")
            else:
                print("You win!")
            quit_game()
        if verb == "go":
            if len(action) == 1:
                print("Sorry, you need to 'go' somewhere.")
                continue
            direction = action[1]
            HP = HP - 1
            current_room = go(world_state, current_room, direction)
        elif verb == "look":
            look(world_state, current_room)
        elif verb == "get":
            if len(action) == 1:
                print("Sorry, you need to 'get' something.")
                continue
            item = action[1]
            get(world_state, current_room, inventory_items, item)
        elif verb == "drop":
            if len(action) == 1:
                print("Sorry, you need to 'drop' something.")
                continue
            item = action[1]
            drop(world_state, current_room, inventory_items, item)
        elif verb == "inventory":
            inventory(inventory_items)
        elif verb == "quit":
            quit_game()
        elif verb == "help":
            help_command()
        else:
            print("Sorry, I don't understand that command.")

    except EOFError:
        print("\nUse 'quit' to exit.")
        continue



