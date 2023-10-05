def play_treasure_island():
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    forfeit = False

    # Crossroad: Right or Left
    choice = input(
        'You\'re at a crossroad. Where do you want to go? Type "Left" or "Right"\n-> ').casefold()

    if choice == "right":
        fate = "You fall into a hole. Game over."
        return fate
    elif choice != "left":
        forfeit = True

    # Lake: Wait or Swim
    choice = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n-> '
    ).casefold()

    if choice == "swim":
        fate = "You were attacked by an angry trout. The wound does not heal. You die of sepsis. Game over."
        return fate
    elif choice != "wait":
        forfeit = True

    if forfeit != True:
        choice = input(
            "You arrive at the island unharmed. There is a house with 4 doors. One red, one orange, one yellow, one green. Which color do you choose?\n-> ")
        if choice == "orange":
            fate = "You open the door and are blasted by a mysterious crimson fire. Within seconds, the extreme heat burns you to ash. Game over."
            return fate
        elif choice == "green":
            fate = "You enter a field of rodents. Rats, racoons, squirrels, mice, and capybara. Rodents you cannot name. Thousands? Millions? You cannot say. Covering the rolling hills, in every direction, beyond the horizon, are rodents. The rodents beneath your feet shift and you lose your balance. There is no door behind you. There are no hills, no soil, no earth. Only rodents atop rodents. You are engulfed and devoured. Game over."
            return fate
        elif choice == "yellow":
            fate = "You found the treasure! You win! Enjoy your shiny yellow treasure."
        elif choice == "red":
            fate = "An unusually tall figure looms over you. A man, a woman? You cannot tell. They wear a dark robe with a large oversized hood. The robe appears to be soiled. Glistening with a dull reddish sheen, it looks sticky and smells of iron. Shrouded in the hood, you can make out only one feature on the face: teeth. The teeth are grotesque. Oversized, dull, and so crooked that some appear to point forward. There are no lips. Only tattered bits of flesh remain. Fear itself consumes you, literally. Game over."
        else:
            forfeit = True

    if forfeit == True:
        fate = "Your indecisiveness and nonconforming choices sealed your fate. You become disoriented. Time itself seems to crumble. The house is gone. Your feet blister on the hot sand. There is no lake around you. Nothing remains but sand and cloudless sky. You wither beneath the scorching sun. Your desiccated remains are tumbleweed, carried to Nowhere by an impartial, unforgiving wind. Your name is lost to history. Game over."
    return fate


fate = play_treasure_island()
print(fate)
