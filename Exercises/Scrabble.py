# Scrabble: Freeform project using dictionaries
# credit: Codecademy (Python 3)


# The focus of this project is to process data from a game of scrabble, using dictionaries to organize players, words, and points.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Update the letters list to contain lowercase letters
letters += [letter.lower() for letter in letters]

points *= 2

# Using list comprehension, create a dictionary that has key value pairs of letters and points.
# Make sure to add the infamous blank scrabble tile.
letter_to_points = {key:value for key, value in zip(letters, points)}

letter_to_points[" "] = 0

print(letter_to_points)

# Create a function that will take in a word and return the point value of that word. 
# If the letter is not in the dictionary, add 0 to the point total.
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter,0)
  return(point_total)

# Test the function.
brownie_points = score_word("BROWNIE")

print(brownie_points)

# Create a dictionary that maps scrabble players to a list of words they have played.
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"], 
    "wordNerd": ["EARTH", "EYES", "MACHINE"], 
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"], 
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
    }

# Create an empty dictionary to track the points for each player.
player_to_points = {}

# Iterate through the player_to_words dictionary and assign each player to player and each list of words to words. 
# Create another loop that calculates the value of each player's words and adds it to a points variable.
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points

update_point_totals() 
      
# Create a function that takes in a player and word and adds it to the player_to_words dictionary
def play_word(player, word):
  player_to_words[player].append(word)

print(player_to_words)

# Turn nested loops into a function that can be called any time a new word is played - addition line 43


