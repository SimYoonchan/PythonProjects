low = 1
high = 1000
number_of_guesses = 1

#Instructions:
print("Welcome to Yoonchan (Charlie) Sim's third Python Project (Equation) - Guess the number")
print()
print("\u0332".join("Instructions "))
    #I found this underline trick at: https://pysnakeblog.blogspot.com/2019/09/python-underline-string-python.html
    #I had to add an extra space to make sure that the underline went all the way till the last character.
print("""You as the player have to pick a number between 1 and 1000.
The purpose of this is to confirm an equation that allows the computer to guess your number in maximum 10 tries. 
This equation works if the number is between 1 and 1000. 

The computer will make a guess.
If the computer guess should be higher, input 'higher'.
If the computer guess should be lower, input 'lower'.
If the computer guess is correct, input 'correct'.
Don't worry about capitals or quotations.""")
print()


#Let's test this equation:
print("\u0332".join("Let's test this equation! "))
      #I found this underline trick at: https://pysnakeblog.blogspot.com/2019/09/python-underline-string-python.html
      #I had to add an extra space to make sure that the underline went all the way till the last character.

while low != high:
      computer_guess_calculation = low + (high - low)//2
            #This calculation ensures that since 2^10 is 1024, and since 1000 is lower than 1024, the computer will only need max 10 guesses.
            #This code has to be in the while loop for the calculation to repeat.
      print("The computer's guess #{} is {}"
                  .format(number_of_guesses, computer_guess_calculation))
      print("\tThe computer's guess is between {} and {}."
            .format(low, high))
      player_statement = input("Your move. Type 'higher', 'lower', or 'correct': ").casefold()
            #Writing casefold here ensures that I don't have to write casefold() for all ifs, elifs,
      print()

      if player_statement.casefold() == 'higher':
            low = computer_guess_calculation + 1

      elif player_statement == 'lower':
            high = computer_guess_calculation - 1
      elif player_statement == 'correct':
            print("The computer's guess of {} is correct."
                  .format(computer_guess_calculation))
            print("The computer found to answer in {} guesses."
                  .format(number_of_guesses))
            break
      else:
            print("Did you correctly type 'higher', 'lower', or 'correct'? Make sure not to put in spaces. Let's try again.")
            print()
      number_of_guesses += 1
            #we keep this code here since code is synchronous and will reach the bottom of this while loop each cycle.
else:
      print("The player thought of the number {}. I got it in {} guesses"
            .format(low, number_of_guesses))