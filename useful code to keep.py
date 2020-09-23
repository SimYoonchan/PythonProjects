game_map = {}
#This is the dictionary holding all the tiles of the game.
tiles = range(101)
#This is the total number of tile spots of the game.
#FILLING UP THE GAME MAP:
for i in tiles:
    game_map[i] = "Tile "+ str(i)
    #The square bracket is indexing.
    #I had to str(i) to concatenate the string "Position ".
    #Doing this filled the game_map dictionary.
    #https://stackoverflow.com/questions/30280856/populating-a-dictionary-using-for-loops-python
print(game_map)