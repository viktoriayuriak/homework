
import sys
import argparse
import re

from sys import exit
from sys import argv

script= argv
prompt = '> '


print ("This is the name of the script: ", script) 
print('============================================================')
print('                  MONKEY AND BANANA GAME!                   ')
print('============================================================')


parser = argparse.ArgumentParser(description = 'This is text game Monkey and bananas')
#print(description)

print("""There are 2 rooms, in one of those rooms are bananas, help monkey find it, 
because she is very HUNGRY""")
print('1 door from the left side and 2 door from the right side')
print('Which door monkey should choose?')
print("""Press #1 and Monkey select door from the left, 
	#2 - Monkey select door from the right""")
print('\n')

door = int(input('Please enter a choice '))
print('\n')
#door = raw_input('>>> ')

#function to choose a door, left or right
def door_selection():
	print('There is no any bananas, sorry')
	print('\n')
	exit_choice = int(input('Does Monkey want to exit? YES - press #1, NO - press #2 '))
	if exit_choice == 1:
		return exit()

	if exit_choice == 2:
		#choice == 2
		return 'This is right Monkey decision!!!'
        #door == 2


#Monkey selected door from the left side
if door == 1:
    print ('This is dark empty room. Monkey should choose another door!')
    print ('What do Monkey want to do?')
    print ('She can try to find some bananas in the middle of the room.')
    print ("""If she wants to try to find it please press #1, if not, press #2 to go out from
this room and choose another door""")
    print('\n')
   
    choice = int(input('Please enter Monkey choice to select door '))

    if choice == 1:
        door_selection()
        
    if choice == 2:
        print('This is right Monkey decision')
        print('Press #2 to enter another door')

elif door == 2:
    print('In the center of the room Monkey can find bananas, this is right room')
    print('\n')
    print ('Press #1 to observe room ')
    print ('Press #2 to exit ')

room_choice = int(input('Please enter Monkey choice #1 room from the LEFT, #2 - room from the RIGHT '))
print('\n')
    
if room_choice == 1:
	print("""Monkey can see a bananas in the middle of room
a bunch of bananas, beyond the monkey's reach, because 
bananas have been hung from the center of the ceiling of the room
in the corner of the room there is a chair""")
	print('\n')
	        	
	print('Press #1 if you want to move')
	print('Press #2  to game over')
	print('\n') 
        	
	move_choice = int(input('Please enter Monkey choice '))

	if move_choice == 1:
		print('Monkey have a chance to reach it')
		print('\n')

		print("""#left - Move left
#right - Move right
#forward - Move forward
#back - Move back""")

		print('\n')

		#Monkey should select a direction to move
		move_directions = ['left', 'right', 'forward', 'back']
		direction_choice = input('Please select Monkey direction ')
		print('\n')


		#WHEN MONKEY MAKE correct DIRECTION (forward)
		def right_direction():
			print('Monkey can see a chair and bananas!!!')
			print('This is correct direction keep moving forward until monkey find a chair')
			print('\n')
			print('Is Monkey found a chair??')


			chair_found = input('Type #yes or #no ')

			while chair_found == 'yes':
				print('Monkey found it! But also Monkey see a bananas!!!')
				print('She wants to take bananas, but cannot reach it when she is jumping ')
				print('Monkey can stand on a chair and try to reach bananas')
				print('\n')


				choice_stand = input('Do you want Monkey do this? (yes/no)? ')

				if choice_stand == 'yes':
					print ( """Monkey is trying to stand on a chair' \n
					 Monkey can reach a bananas. YOU ARE WINNER!!!""")
					exit()


				if choice_stand == 'no':
					print( """Monkey will never reach those bananas, GAME OVER!'
				Monkey is blind, Maybe? :-)))""")



		if direction_choice == move_directions[0]:
			print("From the left side no chair found, Monkey should select another direction")
			print('\n') 

			direction_choice_again = input('Please Monkey should select another direction, except of LEFT ')
			if (direction_choice_again == move_directions[1]):
				print('From the right no any chair and bananas')
				print('GAME OVER')

			if (direction_choice_again == move_directions[2]):
				right_direction()


			if (direction_choice_again == move_directions[3]):
				print('From the back side no any bananas')
				print('GAME OVER')



		elif direction_choice == move_directions[1]:
			print("From the right side no chair found, Monkey should select another direction")
			print('\n')


			direction_choice_again = input('Please Monkey should select another direction, except of RIGHT ')
			if (direction_choice_again == move_directions[0]):
				print('From the left no any chair and bananas')
				print('GAME OVER')

			if (direction_choice_again == move_directions[2]):
				right_direction()


		elif direction_choice == move_directions[2]:
			right_direction()


		elif direction_choice == move_directions[3]:
			print("From the back side no chair found, please select another direction")
			print('\n')


			direction_choice_again = input('Please Monkey should select another direction, except of BACK ')
			if (direction_choice_again == move_directions[0]):
				print('From the left no any chair and bananas')
				print('GAME OVER')

			if (direction_choice_again == move_directions[2]):
				right_direction()

			if (direction_choice_again == move_directions[1]):
				print('From the right no any chair and bananas')
				print('GAME OVER')


#when Monkey selected another room
elif room_choice == 2:
		print('this is empty room, Monkey should try select another door')
		wrong_choice = int(input('press #1 and Monkey can start from the very beginning '))

		if wrong_choice == 1:
			print('GAME OVER!!!')
			exit() #game over and monkey are left hungry
    

