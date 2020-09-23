import random
game_choice = ["rock", "paper", "scissors"]
    #These are the 3 options. This is a list with square brackets. Don't forget to put lists in quotations!
game_over = "quit"
number_of_player_wins = 0
number_of_computer_wins = 0


#Instructions:
print("Welcome to Yoonchan (Charlie) Sim's first Python Project (Game) - Rock, Paper, Scissors")
print()
print("\u0332".join("Instructions "))
    #I found this underline trick at: https://pysnakeblog.blogspot.com/2019/09/python-underline-string-python.html
    #I had to add an extra space to make sure that the underline went all the way till the last character.
print("""You as the player has to pick one of the three options: Rock, Paper, or Scissors.
Don't use any quotations and don't worry about capitals.
Rock wins over Scissors.
Scissors win over Paper.
Paper wins over Rock.
If both the player and the computer choose the same option, you go again.
The game is best 5 out of 7.
You can also stop the game since no one is forcing you to play. Just type '{}'."""
      .format(game_over))
print()


#Let's play best 5 out of 7:
print("\u0332".join("Let's play! "))
    #I found this underline trick at: https://pysnakeblog.blogspot.com/2019/09/python-underline-string-python.html
    #I had to add an extra space to make sure that the underline went all the way till the last character.
player_move = ''
    #we use this as a placeholder to define what player_move is for the while loop

while True:
    player_move = input("Your move. Type rock, paper, or scissors: ").casefold()
        #You have to write the .casefold here before all the if statements for it to work.
    if player_move == 'quit'.casefold():
        print("Game over.")
        break
        #I placed the 'quit' before the computer's turn and before all the if statements so that when the player types quit, it doesn't say anything else.

    computer_move = random.choice(game_choice)
        #I learned this code in -->
            # https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
            #https://pynative.com/python-random-choice/
    print("The computer decided with: {}".format(computer_move))

    if player_move in game_choice:
        if player_move == computer_move:
            print("It's a tie. Go again.")
            print()
        elif player_move == 'rock' and computer_move == 'paper':
            print("Computer wins this round.")
            number_of_computer_wins += 1
            print()
        elif player_move == 'rock' and computer_move == 'scissors':
            print("Player wins this round.")
            number_of_player_wins += 1
            print()
        elif player_move == 'paper' and computer_move == 'scissors':
            print("Computer wins this round.")
            number_of_computer_wins += 1
            print()
        elif player_move == 'paper' and computer_move == 'rock':
            print("Player wins this round.")
            number_of_player_wins += 1
            print()
        elif player_move == 'scissors' and computer_move == 'rock':
            print("Computer wins this round.")
            number_of_computer_wins += 1
            print()
        elif player_move == 'scissors' and computer_move == 'paper':
            print("Player wins this round.")
            number_of_player_wins += 1
            print()
        print("""\t Player at {} rounds won vs Computer at {} rounds won.    
        """
              .format(number_of_player_wins, number_of_computer_wins))
    else:
        print("Wait. Did you type either 'rock', 'paper', or 'scissors' correctly? Remember don't worry about capitals or quotations! Try again.")
        print()

    if number_of_computer_wins == 5:
        print("Computer has won 5 out of 7. Computer wins!")
        break
    if number_of_player_wins == 5:
        print("Player has won 5 out of 7. Player wins!")
        break