# My name is Liu, Kevin.

# The dictionary links a room to other rooms and items associated in the rooms
rooms = {
    'Hallway': {'South': 'Living Room', 'North': 'Master Bedroom', 'West': 'Bedroom', 'East': 'Study Room'},
    'Study Room': {'South': 'Kitchen', 'North': 'Closet', 'West': 'Hallway', 'Item': 'Money'},
    'Master Bedroom': {'South': 'Hallway', 'Item': 'Wig'},
    'Bedroom': {'East': 'Hallway', 'Item': 'Phone'},
    'Living Room': {'North': 'Hallway', 'Boss': 'Babysitter'},
    'Closet': {'South': 'Study Room', 'Item': 'Pillows'},
    'Kitchen': {'North': 'Study Room', 'South': 'Cupboard', 'Item': 'Blankets'},
    'Cupboard': {'North': 'Kitchen', 'Item': 'Code'}
}

# Items picked up will enter the inventory list
inventory = []

# Tracks current room and starting room will be Hallway
current_room = 'Hallway'

# Result of last move
msg = ''


# Define intro so the player will have a little background
def intro():
    print('Welcome to Escape the Babysitter')
    print()
    print('You are in your first year in high school and there is an amazing party happening this weekend at your best')
    print('friends house, but your parents already said no. However; they are on vacation to Hawaii this weekend and')
    print('they hired Mrs. Butters the next door neighbor and she is very mean. You know she will say no and you')
    print('really want to go to this party. Now collect all the items to escape and make sure to avoid the')
    print('Babysitter ')
    print()
    print('Use keywords "Go" followed by North, South, East, and West to move around and "Get" to grab items')


# Display introduction for background
intro()

# Game loop
while True:

    # Display current information
    print(f'You are in the {current_room}\ninventory : {inventory}\n{"-" * 57}')
    print(msg)

    # Item indicator looking it up in the dictionary
    if 'Item' in rooms[current_room].keys():
        nearby_item = rooms[current_room]['Item']
        if nearby_item not in inventory:
            print(f'You see {nearby_item}')

    # Win or Lose
    if 'Boss' in rooms[current_room].keys():

        if len(inventory) > 5:
            print('You escaped.\n'
                  'Stay tuned for part 2!')
            break

        else:
            print('Mrs. Butters was waiting for you!\n'
                  'Game over!')
            break
    # Prompt user for input
    user_input = input('What is your next move?\n')

    # Define moves by splitting into words
    next_move = user_input.split(' ')

    # Define keywords Go and Get. Title so that lower and uppercase don't matter
    action = next_move[0].title()

    # Setting up item pick up and direction of movement to correlate with dictionary
    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = ' '.join(item).title()

    if action == 'Go':

        # Using try so that if player enters crazy input the game won't break
        try:
            current_room = rooms[current_room][direction]
            msg = f'You traveled {direction}.'

        # Using except as a catch all
        except:
            msg = "You can't go that way."

    elif action == 'Get':

        # Using try so that if player enters crazy input the game won't break
        try:

            if item == rooms[current_room]['Item']:

                if item not in inventory:
                    inventory.append(rooms[current_room]['Item'])
                    msg = f'{item} retrieved!'

                else:
                    msg = f'You already have the {item}.'

            else:
                msg = f"Can't find {item}"

        # Using except as a catch all
        except:
            msg = f"Can't find {item}"

    # Exit game
    elif action == 'Exit':
        break
    else:
        msg = 'Invalid Command'
