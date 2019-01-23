#!/usr/bin/python3

"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right"""

import random
def GuessNumber(arb_num, user_input):
	if arb_num == user_input :
		print("Congralution!!!!your guess is correct ")
	elif arb_num - user_input < arb_num/2 :
		print("You are near to the guess ")
	else :
		print("You are far away to the guess ")




arb_num = random.randint(1,9)
print(arb_num)
user_input = int(input("enter any number between 1 and 9"))
GuessNumber(arb_num,user_input)