#! /usr/bin/env python3
# Philip Murphy
# C00222129
# 17/2/17
# Assignment-1 Q2, Number Checking Game
import random
import time
 

end = 0

while end == 0: # While loop allows user to play game for as long as they want

	print('Please enter the amount of guesses that you would like to make at guessing the number I am thinking')


	no = 0   # This while loop is validating the first input to make sure its a number. If the user enters anything other than a number 
		# the loop will continue to ask the user to enter a number
	while no == 0:
		try:
			num = int(input()) # Seting the number of guesses the user wants
			no = 1
		except ValueError:
			print('Not a number please enter a number')	


	# Number generated will be in range of the number they picked multiplied by 10

	size = num * 10 # This gets the size limit for random number

	print('The number is  between 1 and ' + str(size))

	myNum = random.randint(1, size)# 

	print(myNum) # shows random number for testing purposes

	count = 0 # variable used to count the number of times the second while loop iterates

	numOfGuesses = num # variable used to keep track of how many guesses the user has left

	while count < num:# loop will cotinue for the amount of guesses the user entered
		
		print('Number of guesses left ' + str(numOfGuesses))
		print('Wait... ')
		time.sleep(2)# This adds a 2 second time delay so that the all the print isnt printed to the screen at the same time 
		print('Enter your choice')
		numOfGuesses = numOfGuesses - 1

		val = 0   # This while loop validates each guess to make sure that it is a number 
		while val == 0:
			try:
				choice = int(input())
				val = 1
			except ValueError:
				print('Not a number please enter a number')

		if choice == myNum:# if user gets number this message will be displayed
			print('Congratulations you got my number')
			count = num

		elif choice != myNum and count == num - 1:# if choice doesnt equal the number and the count is up then the game is over and the loop break
			print('Game Over')
			break

		else:# this message will print every time the user enters a number unless it is their last chance
			print('Wrong!! Pick Again')
			print(' ')
			count += 1

			if choice > myNum:
				print('My number is lower')

			else:
				print('My number is higher')

	print('Press 0 to continue, Press any other key to quit')# this allows the user to quit or contine the game
	i = input()
	if i ==str(0):# to continue type 0 
		end = 0
	else:		# to quit type any other key
		end = 1