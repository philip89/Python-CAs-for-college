#! /usr/bin/env python3
# Philip Murphy
# C00222129
# 17-2-17
# Assignment-1 Q3, Two Player Dice Game

import random
import time
print('This is a simple dice game with two modes Higher and Lower. In higher mode the aim is to throw a higher number than the computer in lower mode the aim is to throw a lower number than the computer. The game lets you choose how many throws you want to take and how many dice you want to use. You can use up to three dice. Each time you through you will be shown the score and who won that round after the game you will be shown who won the game and asked if you would like to pay again. Press enter when you are ready to start')
start = input()
end = 0
print('Please enter your name')
name = input()
print(' ')
while end == 0:# This while loop lets user decide when to quit playing

###################################################################################################################
# Finding out which game the user wants to play

	print('Hi ' + str(name) + ' which game would you like to play higher or lower, type h or l')
	g = 0
	while int(g) == 0:	 # Used to verift if usr input for game mode
		gameMode = input().lower() # Turns all letters to lower case for comparrison 
		if str(gameMode) == 'h':
			gameMode = 'h'
			g = 1		
		elif str(gameMode) == 'l':
			gameMode = 'l'
			g = 1
		else:		# This will execute if wrong value is entered for game mode
			print('Invalid input. Please enter h for higher or l for lower')
			g = 0

####################################################################################################################
# Finding out how many throws the user wants to take

	print(' ')
	print('How many throws do you want')
	n = 0
	while n == 0: # Loop used to validate input for number of throws
		try:	# Validates if input is a number
			throws = int(input())
			n = 1
			if int(throws) > 9:#This is if the user puts in a number thats to high for throws to see if the did it accidently
				print('Thats an awfull lot of throws are you sure you want that many Y/N')
				con = input().lower()
				if con == 'y':
					n = 1
				elif con == 'n':
					print('Choose again')
					n = 0
				else:
					print('Sorry didnt understand that please choose how many throws you would like again')
					n = 0
		except ValueError:	# If input is not a number yhis executes
			print('Not a number please pick a number')

#####################################################################################################################
# Finding out how many dice the user wants to use

	print(' ')
	print('How many dice?')
	n1 = 0
	while n1 == 0:# loop used to validate the number of dice
		try:		#Validates if it is a number
			noOfDice = int(input())
			n1 = 1
			if int(noOfDice) > 3 or int(noOfDice) < 1:# If statment makes sure users chooses between 1 and 3 dice
				print('You must only use 1, 2 or 3 dice please pick again')
				n1 = 0
		except ValueError:# If a non number is input this executes
			print('Not a number please enter a valid number')

######################################################################################################################
# The following chunk of code is used for playing the dice game

	pScore = 0# Variables to keep track of scores
	cScore = 0

	
	for e in range(throws): #For loop loops for as many throws as the user would like to take

		for i in range(noOfDice):# for loop used to generate random numbers for amount of dice needed
			pDice = 0# Used to save users and computers score when more than one dice is rolled
			cDice = 0
			pRand = random.randint(1,6)# Users dice
			cRand = random.randint(1,6)# Computers dice
	#print(pRand).............Used these values to look at the random numbers while testing
	#print(cRand)
			pDice =  pDice + pRand
			cDice =  cDice + cRand
	# pDice = 9..............Used these values to test what would happen in the event of a draw
	# cDice = 9
		print('------------------------------')	
		print('Rolling ' + str(name) + 's dice...')# This set of print statments is used to simulate rolling of dice
		time.sleep(1.5) 
		print(str(name) +' ..... ' + str(pDice))	
		print(' ')
		print('Rolling my dice....')
		time.sleep(1.5)
		print('Computer .....  ' + str(cDice))
		time.sleep(1.5)
		print(' ')
			
		if pDice > cDice:		# These If statments decide what output the user will see depending on type of game they choose
			if gameMode =='h':
				pScore += 1
				print('You win')
			elif gameMode == 'l':
				cScore += 1
				print('You loose')
		elif pDice < cDice:
			if gameMode == 'h':
				cScore += 1
				print('You loose')
			elif gameMode == 'l':
				pScore += 1
				print('You Win')
		else:
			print('Same score, Its a draw')
		print(' ')
		print('Score')
		print(str(name) + ' '+ str(pScore))
		print('Computer: ' + str(cScore))
		print('------------------------------')
		time.sleep(3)
		print(' ')
	

#####################################################################################################################
# Final output which tells the user who won the game and asks would they like to play again

	if pScore > cScore:	# If statments tells user who won the over all game
		print('Congratulations you won this game')
	elif cScore > pScore:
		print('Hard luck, You lost this game. Better luck next time')
	else:
		print('Wow its a draw, We must play again to get a winner')
	time.sleep(2)

	# Find out if user wants to play again
	print('Press 0 to play again, press any other key to quit')
	q = input()
	if q == str(0):
		end = 0
	else:
		end = 1