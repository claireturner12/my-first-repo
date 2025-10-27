import random
VALID_OPTIONS = ["rock", "paper", "scissors"]

# ASK THE USER FOR AN INPUT (R/P/S)

user_choice = input("Please choose one of 'rock', 'paper', or 'scissors':")
print("USER:", user_choice)

# VALIDATIONS

if user_choice not in VALID_OPTIONS:
    print("Oops, invalid input. Please try again.")
    #exit
    quit()

# GENERATE A RANDOM COMPUTER CHOICE

computer_choice = random.choice(VALID_OPTIONS)
print("COMPUTER:", computer_choice)

# DETERMINE THE WINNER
print("TODO:", "Determine Winner")