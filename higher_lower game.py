#import the os to get the clear() function
import os
#This function clear's the console
clear = lambda: os.system('cls')

import random
from game_data import data
from art import logo, vs

#Compare their followers and return the greater one
def compare(item_1, item_2):
	if item_1["follower_count"] > item_2["follower_count"]:
		return 'A'
	elif item_1["follower_count"] < item_2["follower_count"]:
		return 'B'

count = 0
continue_ = True

#Print the logo for the starting page
print(logo)
while continue_:
	#Choose 2 item from game data list item 1 and 2
	if count == 0:
		item_1, item_2 = random.sample(data, 2)
		previous_second_item = item_2

	#If user guesses right take the previous second item as next first item and continue	
	elif count > 0:
		item_1 = previous_second_item
		item_2 = random.choice(data)
		while item_1 == item_2:
			item_2 = random.choice(data)
		previous_second_item = item_2

	
	print(f"Compare A: {item_1['name']}, a {item_1['description']}, from {item_1['country']}")
	print(vs)
	print(f"Compare A: {item_2['name']}, a {item_2['description']}, from {item_2['country']}")

	#Compare their followers and assign it to the result variable
	result = compare(item_1, item_2)

	#Ask user to guess which one has more followers than the other
	ask = input("Who has more followers. Type 'A' or 'B': ").upper()

	#Check if user guessed right
	#If user guesses right, show the current score and continue
	if ask == result:
		count += 1
		clear()
		print(logo)
		print(f"You're right! Current score: {count}")

	#If user guesses wrong, end the game and show the total score
	else:
		clear()
		print(logo)
		print(f"Sorry, that's wrong. Final score: {count}")
		continue_ = False
		
		