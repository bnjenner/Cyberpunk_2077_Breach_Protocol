'''
BEACH ACCESS POINTS IN CYBERPUNK 2077

RULES:
	Traverse rows and columns to find path fulfilling all 
		hexcodes in sequences in their respective orders.
			1. Order individual sequences are chosen in do not 
				matter, but the order within each sequence does.
			2. Once a cell is picked, it cannot be picked again
			3. Total number of codes provided must be equal to
				or less than buffer size.
			4. If additional space in buffer, a wrong choice can
				be made to adjust position and fulfill additional
				sequences, correcting errors in path finding 
				or making the puzzle possible at all.

NOTES
	- Need to deal with branching solutions
		Probably convert string path to list and have nested lists representing
		branching solutions
	- Does not consider doubles (when one selection counts for two codes)
	- Does not account for error capacity
	- Add cyberpunk asthetic to print statements, lol
'''

##########################################################################################
# imports 
import sys
import itertools

##########################################################################################
# Global Variables

# Found from: https://emojicombos.com/cyberpunk-2077-ascii-art 
UNNECESSARY_INTRO = """
////////////////////////////////////////////////////////////////////////////////

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⡔⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢚⣉⣠⡽⠂⠀⠀⠀⠀⡰⢋⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢴⡆⠀⠀
⠀⠀⠀⠀⠀⢀⡤⠐⢊⣥⠶⠛⠁⢀⠄⡆⣠⠤⣤⠞⢠⠿⢥⡤⠀⠀⠠⢤⠀⠀⠀⠤⠤⠤⡄⢠⠤⠄⠤⠀⠀⠀⠒⣆⡜⣿⣄⠀⡤⢤⠖⣠⣀⠤⢒⣭⠶⠛⠃⠀⠀
⢀⣀⡠⢴⣎⣥⣴⣾⣟⡓⠒⠒⠒⠺⣄⡋⢀⡾⢃⣴⢖⣢⣞⢁⣋⣉⣹⠏⠚⠛⢛⣉⣤⡴⢞⠃⣰⠾⠟⣛⣩⢵⢶⡟⣰⠇⠘⡼⢡⡟⣀⡋⢵⡞⠋⠁⠀⠀⠀⠀⠀
⠈⠢⠄⠤⠤⠤⠤⠤⠴⠤⠴⠶⠶⢾⠟⣱⡿⢤⢿⣕⠾⣿⣿⣩⡭⢤⠞⣰⠶⢤⣀⡉⠓⢾⡍⣠⠴⠾⠛⠹⠡⣟⡁⢰⢏⣼⡇⢰⣿⢀⠟⠳⣤⣌⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢃⡼⠋⠛⠾⠚⠁⠀⠈⠉⠀⠀⠸⣄⠏⠀⠀⠈⠙⠓⡟⣰⠏⠀⠀⠀⠘⠾⠛⠳⠞⠉⠁⠙⠋⠙⠚⠀⠀⠀⠙⠛⢿⣷⣤⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣜⡵⠟⠀⠀⠀⠀⠀⠀⣼⣿⣾⣿⣽⣽⣿⣿⢏⢫⣻⡹⡽⣰⢏⣯⠍⡭⡍⣭⢩⡭⢩⡍⡏⡏⣯⡍⣍⠙⡭⢹⣄⣤⠄⢠⠉⠓⢿⣕⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣯⠃⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣽⣾⣾⣟⣯⣣⣱⣾⣟⣞⣸⣇⣳⣃⣿⣛⣷⣬⠧⠳⠇⠿⢧⢿⢀⣷⢸⠧⢾⢃⠇⠀⠀⠀⠀⠁


////////////////////////////////////////////////////////////////////////////////""".strip()


BUFFER_SIZE = 8

# solvable for all sequences 
SEQUENCES = [["BD", "1C"],
			 ["1C", "1C", "E9"],
			 ["1C", "1C", "BD"]]

# # not solvable for all sequences 
# SEQUENCES = [["BD", "E9"],
# 			 ["1C", "1C", "E9"],
# 			 ["1C", "1C", "BD"]]


#	Solvable for all sequences
FRAME = [["BD", "E9", "1C", "BD", "1C"],
		 ["55", "55", "55", "1C", "E9"],
		 ["1C", "BD", "BD", "55", "1C"],
		 ["55", "1C", "1C", "BD", "55"],
		 ["1C", "55", "BD", "1C", "1C"]]


ERROR_CAP = BUFFER_SIZE - sum(map(len, SEQUENCES))



##########################################################################################
# Functions

# This set of functions is completely unnecessary, but cool for the cyberpunk vibe
#	Modified from this forum response: https://stackoverflow.com/questions/39473297/how-do-i-print-colored-output-with-python-3
def print_fail(message, end = '\n'):
	sys.stderr.write('\x1b[1;31m' + message + '\x1b[0m' + end)

def print_pass(message, end = '\n'):
	sys.stdout.write('\x1b[1;32m' + message + '\x1b[0m' + end)

def print_warn(message, end = '\n'):
	sys.stderr.write('\x1b[1;33m' + message + '\x1b[0m' + end)

def print_info(message, end = '\n'):
	sys.stdout.write('\x1b[1;34m' + message + '\x1b[0m' + end)

def print_result(message, code, end = '\n'):
	sys.stdout.write(message + '\x1b[1;33m' + code + '\x1b[0m' + end)


#############################################
# Function for finding index of hexcode in row or column of matrix
def index_finder(sequence, hexcode, row, index, prev_index, depth, exclude_list):

	# Takes possible hex codes to find,
	#	a boolean designating to look for rows or columns (true if row, false if column),
	#	the index to search use for rows or columns,
	#	the previous index,
	#	the depth of the search (length of answer sequence),
	#	and the index to exclude (NOT ALWAYS THE SAME AS PREVIOUS INDEX),
	#	and rows or columns.
	#	Outputs index or code indicating certain conditions met.

	# get correct row or column
	if row:
		line = FRAME[index]
	else:
		line = [row_col[index] for row_col in FRAME]

	# print("\tSearching for ", hexcode, " in ", line, "...", sep = "")

	# find indicies of matching hex codes
	for i in range(len(line)):

		# get proper coordinates being checked
		if row:
			coord = str(prev_index) + str(i)
		else:
			coord = str(i) + str(prev_index)
		
		if not coord in exclude_list:

			# if hexcode match
			if line[i] == hexcode:

				# print("\t    Found in position", i)

				exclude_list.append(coord)

				# if buffer size is reached 
				if depth == len(sequence) - 1:
					# print("\tSolution found!")
					return str(i) + "+"

				# get new hexcode 
				new_depth = depth + 1
				new_row = not row

				#	if buffer size is met
				if depth >= BUFFER_SIZE - 1:
					# print("\tBUFFER REACHED!!!")
					return "!"
				
				# new hexcode to find
				new_hexcode = sequence[new_depth]

				# print("\t    New hexcode target is", new_hexcode)
				# print("\t    Searching at depth", new_depth)
				# print("\t    Excluding", exclude_list)

				tmp_str = (str(i) + index_finder(sequence = sequence,
												 hexcode = new_hexcode,
												 row = new_row,
												 index = i,
												 prev_index = i,
												 depth = new_depth,
												 exclude_list = exclude_list))

				if tmp_str[-1] != "-":
					return tmp_str

	return "-"


#############################################
# Wrapper function for index_finder
def breach_protocol(sequences):

	# Takes sequences, generates all possible combinatinos
	#	sequences, and iterates through them with index_finder.
	#	Returns possible path answers

	answers = []

	# get all possible string combintations
	sequence_strings = list(map("".join, sequences))
	possible_sequences = ["".join(s) for s in list(itertools.permutations(sequence_strings, 3))]
	
	# iterate through possible paths and check them
	for seq in possible_sequences:

		# split sequence string into list
		list_seq = [seq[i:i + 2] for i in range(0, len(seq), 2)]
		hexcode = list_seq[0]

		print("  //BREACHING SEQUENCE: " + str(list_seq))
		result = index_finder(sequence = list_seq,
							  hexcode = hexcode, 
							  row = True,
							  index = 0,
							  prev_index = 0,
							  depth = 0,
							  exclude_list = [])

		# if solution found, format path as coordinates
		if result[-1] == "+":

			print_pass("  //BREACHING_STATUS..................................................COMPLETE")
	
			# formate path outputs and append to answers tab		
			path = "['0" + result[0] + "', "
			for i in range(1, len(result) - 1):

				if i % 2:
					path += "'" + result[i] + result[i - 1] + "', "
				else:
					path +=  "'" + result[i - 1] + result[i] + "', "
			
			answers.append([str(list_seq), path[:-2] + "]"])

		else:
			print_fail("  //BREACHING_STATUS....................................................FAILED")

	print_info("[ ALL SEQUENCE UPLOADS TESTED ]")

	return answers



##########################################################################################
# main function	
def main():

	print_warn(UNNECESSARY_INTRO)
	print_info("[ ENGAGING BREACH PROTCOL... ]")
	
	# Find breach solutions
	solutions = breach_protocol(SEQUENCES)

	# check if solutions
	if len(solutions) == 0:

		# print failure message
		print_fail("[ NO SUCCESSFUL SOLUTIONS IDENTIFIED ]")
		print_fail("  //ROOT_ATTEMPT_1")
		print_fail("  //ROOT_ATTEMPT_2")
		print_fail("  //ROOT_ATTEMPT_3")
		print_fail("  //ROOT_FAILED")
		print_fail("  //ROOT_REBOOT")
		print_fail("  //ACCESSING.............................................................FAILED")
		print_fail("  //ACCESSING.............................................................FAILED")
		print_fail("  //ACCESSING.............................................................FAILED")
		print_fail("  //ACCESSING.............................................................FAILED")
		print_fail("  //ACCESSING.............................................................FAILED")
		print_fail("[ USER TERMINATED PROCESS ]")
		print_fail("[ BREACH ATTEMPT FAILED ]")

	else:

		# print success message 
		print_pass("[ SUCCESSFUL SOLUTIONS IDENTIFIED ]")
		print_pass("  //ROOT")
		print_pass("  //ACCESS_REQUEST")
		print_pass("  //ACCESS_REQUEST_SUCCESS")
		print_pass("  //COLLECTING PACKET_1.................................................COMPLETE")
		print_pass("  //COLLECTING PACKET_2.................................................COMPLETE")
		print_pass("  //COLLECTING PACKET_3.................................................COMPLETE")
		print_pass("  //COLLECTING PACKET_4.................................................COMPLETE")
		print_pass("  //LOGIN")
		print_pass("  //LOGIN_SUCCESS")
		print_pass("  //")
		print_pass("  //UPLOAD_IN_PROGRESS")
		print_pass("  //UPLOAD_COMPLETE!")
		print_pass("[ ALL DAEMONS UPLOADED ]")
		print_pass("[ SUCCESSFUL INPUTS: " + str(len(solutions)) + " ]")

		# print solutions 
		solution_index = 0
		for path in solutions:
			print_pass("  //INPUT_" + str(solution_index) + "")
			print_result("  //SEQUENCE:         ", path[0])
			print_result("  //COORDINATES:      ", path[1])
			solution_index += 1

	# say goodbye
	print_info("[ BREACHING PROCESS COMPLETE ]")
	print_info("[ EXITING INTERFACE ]")
	print_warn("////////////////////////////////////////////////////////////////////////////////")



if __name__ == '__main__':
	main()



