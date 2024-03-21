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
'''

# import 
import sys
import itertools


# Global Variables
BUFFER_SIZE = 8

FRAME = [["BD", "E9", "1C", "BD", "BD"],
		 ["55", "55", "55", "1C", "E9"],
		 ["1C", "BD", "BD", "55", "1C"],
		 ["55", "1C", "1C", "BD", "55"],
		 ["1C", "55", "BD", "1C", "1C"]]


SEQUENCES = [["BD", "1C"],
			 ["1C", "1C", "E9"],
			 ["1C", "1C", "BD"]]

ERROR_CAP = BUFFER_SIZE - sum(map(len, SEQUENCES))



# Functions
def index_finder(sequence, hexcode, row, index, prev_index, depth, exclude):

	# Takes possible hex codes to find,
	#	a boolean designating to look for rows or columns (true if row, false if column),
	#	the index to search use for rows or columns,
	#	the previous index,
	#	the depth of the search (length of answer sequence),
	#	and the index to exclude (NOT ALWAYS THE SAME AS PREVIOUS INDEX),
	#	and rows or columns.
	#	Outputs index or code indicating certain conditions met.

	#	if sequenece is correct 
	if depth == len(sequence):
		return "+"

	# get correct row or column
	if row:
		line = FRAME[index]
	else:
		line = [row[index] for line in FRAME]


	print("\tSearching for", hexcode, "in", line)

	# find indicies of matching hex codes
	for i in range(len(line)):

		if i != exclude:

			# if hexcode match
			if line[i] == hexcode:

				print("\t\tFound in position", i)

				if depth > 0:
					new_exclude = prev_index
				else:
					new_exclude = 0

				# get new hexcode 
				new_depth = depth + 1

				#	if buffer size is met
				if depth >= BUFFER_SIZE - 1:
					print("\tBUFFER REACHED!!!")
					return "!"
				
				new_hexcode = sequence[new_depth]


				print("\t\tNew hexcode target is", new_hexcode)
				print("\t\tSearching at depth", new_depth)
				print("\t\tExcluding", new_exclude)

				return (str(i) + index_finder(sequence = sequence,
											  hexcode = new_hexcode,
											  row = not row,
											  index = i,
											  prev_index = i,
											  depth = new_depth,
											  exclude = new_exclude))

	
	print("\t\tNo Path Found")
	return "-"


def accesspoint_cracker(sequences):

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

		print("\n\nSTARTING SEQ", list_seq, "!!!\n\n")
		result = index_finder(sequence = list_seq,
							  hexcode = hexcode, 
							  row = True,
							  index = 0,
							  prev_index = -1,
							  depth = 0,
							  exclude = [])

		if result[-1] == "+":
			answers.append(result)

	return answers

		

answers = accesspoint_cracker(SEQUENCES)

for a in answers:
	print(a)



# path_finder(SEQUENCES)


