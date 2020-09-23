import shelve
import random

game_over = 'quit'
game_word = ''
game_word_display = ''
game_strikes = 6
bad_guesses = 0
#Also will have:
#1) hangman_library --> shelve
#2) category_selection --> variable
#3) letters_amount --> variable
#4) player_guess --> variable
#Note: Can accept spaces as input.


#Instructions:
print("Welcome to Yoonchan (Charlie) Sim's third Python Project (Game) - Hangman")
print()
print("\u0332".join("Instructions "))
print("""You are playing the game 'Hangman'! You as the player has to pick a category first.
After typing up the category, a word will be selected by random from this category and you will have 6 strikes for guessing a letter or the word.
Spaces count as a letter placement so press space bar for these!
Punctuations also count as letter placement so press appropriate punctuations for these!
If you get guess the word before the 6 strikes, you win!
If not, you lose!
You can also stop the game since no one is forcing you to play. Just type '{}'.
Ready to play?""".format(game_over))
print()


#Picking a word:
hangman_library = shelve.open('hangman library')

while True:
      category_selection = input("The categories are: " + ", "
                                 .join(hangman_library.keys())
                                 + ". Type the category you want to try: ")

      if category_selection in hangman_library.keys():
            game_word = random.choice(hangman_library[category_selection])
            break
      else:
            print(category_selection + " is not valid. Double check the spelling and upper and lower case!")
            print()
print(game_word)

game_word_display = ['_' for i in game_word] #This goes here since we need 'game_word' first.
while True:
      letters_amount = len(game_word)
      print("Your word is " + str(letters_amount) + " letters long.")
      print(game_word_display)
      print()
      print()

      player_guess = input("Type a letter or guess the word: ")

      if player_guess.casefold() == game_over:
            print("Game over.")
            break

      if bad_guesses == game_strikes:
            print("You went over 6 strikes! You lose!")
            print('Your word was "{}".'.format(game_word))
            break

      for i, letter in enumerate(game_word):
            if letter != "_" and player_guess == letter:
                  game_word_display[i] = letter
                  print("".join(game_word_display))

      if player_guess.lower() not in game_word.lower():
      #This doesn't solve if a letter that is wrong is either capital or lower case.
      #But it at least prevents it from collecting strikes.
            bad_guesses += 1
            print("That is strike {} out of {}!".format(bad_guesses, game_strikes))
            print("".join(game_word_display))

      if player_guess.casefold() == game_word.casefold():
            print("You guessed the word, '{}' correctly before 6 strikes. You win!"
                  .format(game_word))
            break
hangman_library.close()