import random
#import time
    #this will help make dice rolling more anticipatory
    #https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
import sys
    #https://stackoverflow.com/questions/19782075/how-to-stop-terminate-a-python-script-from-running

#VARIABLES:
game_over = ['quit', 'q']
dice_possibility = [1, 2, 3, 4, 5, 6]
snake_down = ["Uh-OH!", "Yikes!", "Too bad!", "Bummer!"]
ladder_up = ["WOOHOO!", "BLESS UP!", "Awesome!", "Up we go!"]
player_names = {}
    #This is a dictionary of player names.
player_limit = range(2, 4)
tile_position_dict = {}
#OTHER VARIABLES:
#1) number_of_players --> input variable
#2) player_slot --> value for player_names
#3) each_player --> control loop variable (for loop)
#4) dice_roll --> variable
#5) dice_roll_dict --> making dice_roll into a list


#INSTRUCTIONS:
print("Welcome to Yoonchan (Charlie) Sim's fourth Python Project (Game) - Snakes and Ladders")
print()
print("\u0332".join("Instructions "))
print("""You are playing the game 'Snakes and Ladders'! 
This game is for 2-3 people only! Once you pick the number of players, you will provide each player with names.
The youngest will go first so this player should write their name first, so the last player is the oldest player!
The rule is simple. Roll the dice by pressing ENTER and get to TILE 100 to win!
There are tiles that will advance you closer to the finish line (ladders) while some tiles brings you down (snakes).
Ready to play?""")
print()


#ENTERING PLAYER AMOUNTS AND PLAYER NAMES, AND CREATING EACH PLAYER'S TILE POSITION:
while True:
    number_of_players = int(input("Enter the number of players (only 2-3 players): "))

    if number_of_players in player_limit:
        for i in range(number_of_players):
            player_slot = "Player " + str(i)
            #player_slot is a key in a dictionary.
            player_names[player_slot] = str(input("Player " + str(i) + ", please type your name: "))
            #What we are inputting here is the value of the
            #corresponding key in a dictionary.
    else:
        print("You need 2, or 3 players.")

    for slot, names in player_names.items():
        print("We have {} playing as {}.".format(names, slot))

    for each_player in player_names.values(): #We state '.values()' so that we can get the player's names.
        tile_position_dict[each_player] = {0}
    break
print()


#GAMEPLAY
print("\u0332".join("Let's play Snakes and Ladders! "))
while True:
    for each_player in player_names.values(): #We state '.values()' so that we can get the player's names.
        print(str(each_player) + ", you are currently on tile position " + str(tile_position_dict[each_player]))
        player_turn = input("{}, press ENTER to roll the dice: ".format(each_player))

        if player_turn.casefold() == game_over:
            print("Game Over.")
            sys.exit()

        dice_roll = int(random.choice(dice_possibility))
        dice_roll_dict = {dice_roll}
        # time.sleep(2)
        print(input("{}, you rolled a {}".format(each_player, dice_roll)))

        tile_position_dict[each_player] = [sum(i) for i in zip(tile_position_dict[each_player], dice_roll_dict)]
            #https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
        print("{}, you are now on tile position {}".format(each_player, tile_position_dict[each_player]))

        if tile_position_dict[each_player] == [3]:
            tile_position_dict[each_player] = [21]
            print(random.choice(ladder_up) + " You moved UP to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [8]:
            tile_position_dict[each_player] = [30]
            print(random.choice(ladder_up) + " You moved UP to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [28]:
            tile_position_dict[each_player] = [84]
            print(random.choice(ladder_up) + " You moved UP to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [58]:
            tile_position_dict[each_player] = [74]
            print(random.choice(ladder_up) + " You moved UP to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [75]:
            tile_position_dict[each_player] = [86]
            print(random.choice(ladder_up) + " You moved UP to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [80]:
            tile_position_dict[each_player] = [100]
            print(random.choice(ladder_up) + " You moved UP to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [90]:
            tile_position_dict[each_player] = [91]
            print(random.choice(ladder_up) + " You moved UP to tile position {}"
                  .format(tile_position_dict[each_player]))

        if tile_position_dict[each_player] == [17]:
            tile_position_dict[each_player] = [13]
            print(random.choice(snake_down) + " You moved DOWN to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [52]:
            tile_position_dict[each_player] = [29]
            print(random.choice(snake_down) + " You moved DOWN to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [57]:
            tile_position_dict[each_player] = [40]
            print(random.choice(snake_down) + " You moved DOWN to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [62]:
            tile_position_dict[each_player] = [22]
            print(random.choice(snake_down) + " You moved DOWN to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [88]:
            tile_position_dict[each_player] = [18]
            print(random.choice(snake_down) + " You moved DOWN to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [95]:
            tile_position_dict[each_player] = [51]
            print(random.choice(snake_down) + " You moved DOWN to tile position {}"
                  .format(tile_position_dict[each_player]))
        elif tile_position_dict[each_player] == [97]:
            tile_position_dict[each_player] = [79]
            print(random.choice(snake_down) + " You moved DOWN to tile position {}"
                  .format(tile_position_dict[each_player]))

        if tile_position_dict[each_player] > [99]:
            print("{}, you have reached the finish. You win! Game Over!"
                  .format(each_player))
            sys.exit()
        print()