import random
from sys import exit

# Returns: Random choice of True or False each time it is called
# Used for adding a strum or a rest in each beat
def beat_or_rest():
	t_or_f = [True, False]

	tf = random.choice(t_or_f)
	if tf == True:
		return True
	else:
		return False


# Creates a random set of strums and rests and adds them to a list,
# Converts the list to a string, and returns the string the designated number of times
def return_beats(length):
	possible_positions = [0,1,2,3,4,5,6,7]
	beats = [0,2,4,6]
	offbeats = [1,3,5,7]
	bar = '|'
	list_of_beats = []
	partial_list = []

	for num in possible_positions:
		if num in beats:
			if beat_or_rest():
				partial_list.append('D')
			else:
				partial_list.append('_')
		elif num in offbeats:
			if beat_or_rest():
				partial_list.append('U')
			else:
				partial_list.append('_')
	partial_list.append('|')
		
	if length == 1:
		list_of_beats.append(bar)
		list_of_beats.extend(partial_list)
		return (''.join(list_of_beats)) * length
	else:
		partial_list_as_string = ''.join(partial_list)
		
		return '|' + partial_list_as_string * length
	
	
# Returns the guide that will be printed above the rhythm
def return_measures(length):
	partial = '1+2+3+4+|'
	full_measure = "|" + partial
	
	if length == 1:
		output = full_measure
	else:
		output = full_measure + partial * (int(length) - 1)
	return output


# Returns any int the user inputs
def pick_length():
	num = raw_input('How many measures do you want? (1-4) ')
	num = int(num)
	return num


# PRINTS the guide and REPEATING RANDOM RHYTHM
def generate_rhythm():
	print "\n\n"
	print return_measures(num)
	print return_beats(num)
	print "\n\n"



# FULL RANDOM_________________________________________________________________

# GO FULL RANDOM
# Creates random rhythm without the first bar, appends it to a list, 
# Converts the list to a string, then returns the string
def return_partial_string():
	possible_positions = [0,1,2,3,4,5,6,7]
	beats = [0,2,4,6]
	offbeats = [1,3,5,7]
	bar = '|'
	
	partial_list = []

	for num in possible_positions:
		if num in beats:
			if beat_or_rest():
				partial_list.append('D')
			else:
				partial_list.append('_')
		elif num in offbeats:
			if beat_or_rest():
				partial_list.append('U')
			else:
				partial_list.append('_')
	partial_list.append(bar)
	partial_list_as_string = ''.join(partial_list)
	return partial_list_as_string

# GO FULL RANDOM
# Creates the first bar, then calls return_partial_string the designated number of times
# And returns that in a final string
def return_all_random_beats(length):
	final_string = "|"

	if length == 1:
		return '|' + return_partial_string()
	else:
		for i in range(1, length + 1):
			 final_string += return_partial_string()
		return final_string

#GO FULL RANDOM
# PRINTS the random beats for the specified number of measures
def go_full_random():
	print "\n\n"
	print return_measures(num)
	print return_all_random_beats(num)
	print "\n\n"



# CREATE & DISPLAY_____________________________________________________________

preset_rhythms = {
	'folk strum': '|D_DU_UDU|D_DU_UDU|',
	'reggae': '|_U_U_U_U|_U_U_U_U|',
	'cypress hill': '|_UD_DU_U|D_DU_UDU|',
	'silence': '|        |        |'
}

def get_created_rhythm():
	print "\n\nType in the rhythm you want to create:"
	print "  |1+2+3+4+|1+2+3+4+|"
	created_rhythm = raw_input("> ")
	return created_rhythm


def print_presets():
	print "\n\nPreset Rhythms"
	print "Type the name of the rhythm you want\n"
	i = 1
	#list_of_titles = []
	for title in preset_rhythms.keys():
		print "{}. {}\n".format(str(i), title)
		#list_of_titles.append(title)
		i += 1

	
	song_choice = raw_input("> ").lower()
	if song_choice in preset_rhythms.keys():
		print "\n\n"
		print song_choice.upper() + ':\n'
		print return_measures(2)
		print preset_rhythms[song_choice]
		print "\n\n"
	else:
		print_presets()


# These two functions will be implemented in the future
def return_created_as_html():
	get_created_rhythm()
	created_rhythm_as_html = "<p>|1+2+3+4+|1+2+3+4+|<br>created_rhythm</p>"
	return created_rhythm_as_html

def return_created_as_string():
	get_created_rhythm()
	return created_rhythm



# User Interaction:____________________________________________________________

while True:
	print("\n\n8TH NOTE GUITAR STRUMMING:\n")
	print('Type "RANDOM" to generate a random rhythm')
	print('Type "DISPLAY" to see preset rhythms')
	print('Type "CREATE" to create your own rhythm')
	print('Hit q to quit')

	choice = raw_input('> ').lower()
	if choice == 'random':
		print('\nType "REPEAT" for a random measure that repeats')
		print('Type "RANDOM" again if you want to randomize every measure')
		second_choice = raw_input("> ").lower()
		# REPEATING random measure
		# If user wants one random measure repeating:
		if second_choice == 'repeat':
			num = pick_length()
			generate_rhythm()
			
			while True:
				again = raw_input("Again? y/n ").lower()
				if again == 'y':
					generate_rhythm()
				else:
					break
		else:
		# GO FULL RANDOM 						
		# If user wants every measure to be random, not one random measure repeating:
			num = pick_length()
			go_full_random()
			
			while True:
				again = raw_input("Again? y/n ").lower()
				if again == 'y':
					go_full_random()
				else:
					break

	# If user wants to display the preset rhythms:
	elif choice == 'display':
		print_presets()

		while True:
			another = raw_input("Pick another rhythm? y/n ").lower()
			if another == 'y':
				print_presets()
			else:
				break

	# If user wants to create their own rhthym, not randomized:
	elif choice == 'create':
		get_created_rhythm()
		go_back = raw_input("Go back? y/n ").lower()
		if go_back == 'y':
			continue
		else:
			print 'bye'
			exit(0)

	elif choice == 'q':
		print '\nbye'
		exit(0)
	else:
		print "That's not one of the options."
		continue

main()


