# Greetings to the project
print("Welcome to the Blackjack card game!")

import random
from art import logo
from replit import clear

#Create a "deal_card()" function that uses the "cards" list to *return* a random card.
#11 is the Ace.
def deal_card():
  """ Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Create a function called calculate_score() that takes a List of cards as input and returns the score
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """ Takes list of cards as input and returns the calculated score """

  #Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of actual score
  #0 will represent a blackjack in our game.
  if sum(cards) == 0 and len(cards) == 2:
    return 0 

  #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. 
  #Need functions of append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins. 
def compare(user_score, computer_score):

  #If both computer and user scores are over 21, user loses. This is bug fix
  if user_score > 21 and computer_score > 21:
    return "Both hands are over 21. You lost"

  if user_score == computer_score: 
    return "It's a draw"
  elif user_score == 0:
    return "You won with Blackjack"
  elif computer_score == 0:
    return "Computer won. You lost"
  elif user_score > 21:
    return "You lost"
  elif computer_score > 21:
    return "Computer lost. You won"
  elif user_score > computer_score:
    return "You won with high hand"
  else:
    return "You lost"

def play_game():
  print(logo)
  
  #Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  is_the_end = False
  
  for i in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    computer_cards.append(new_card)

  #The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  while not is_the_end:
      
    #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends. 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards are {user_cards} and score is {user_score}.")
    print(f"Computer's first card {computer_cards[0]}.")
  
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_the_end = True
    else:
      #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended. 
      user_deal = input("Type 'yes' to take another card, 'no' to pass.")
      if user_deal == "yes":
        user_cards.append(new_card)
      else:
        is_the_end = True

  #Once user is done, it's time to let the computer play. Computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(new_card)
    computer_score = calculate_score(computer_cards)
  
  print(f"Your hand {user_cards} and final score is {user_score}")
  print(f"Computer's hand {computer_cards} and final score is {computer_score")
  print(compare(user_score, computer_score)
      
#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
end = input("Would you like to start a blackjack game? Type 'yes' or 'no'.")
while end:
  if end == "yes":           
    clear()
    play_game()

