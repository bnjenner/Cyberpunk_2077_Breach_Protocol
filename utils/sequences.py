import itertools

from .cybermessages import CyberMessages as msg

##########################################################################################


class SequenceHack:

    # init function
    def __init__(self, FRAME, SEQUENCES, BUFFER_SIZE):
        self.FRAME = FRAME
        self.SEQUENCES = SEQUENCES
        self.BUFFER_SIZE = BUFFER_SIZE

    #############################################
    # Function for finding index of hexcode in row or column of matrix
    def index_finder(
        self, sequence, hexcode, row, index, prev_index, depth, exclude_list
    ):

        # Takes possible hex codes to find,
        # 	a boolean designating to look for rows or columns (true if row, false if column),
        # 	the index to search use for rows or columns,
        # 	the previous index,
        # 	the depth of the search (length of answer sequence),
        # 	and the index to exclude (NOT ALWAYS THE SAME AS PREVIOUS INDEX),
        # 	and rows or columns.
        # 	Outputs index or code indicating certain conditions met.

        # get correct row or column
        if row:
            line = self.FRAME[index]
        else:
            line = [row_col[index] for row_col in self.FRAME]

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

                    # 	if buffer size is met
                    if depth >= self.BUFFER_SIZE - 1:
                        # print("\tBUFFER REACHED!!!")
                        return "!"

                    # new hexcode to find
                    new_hexcode = sequence[new_depth]

                    # print("\t    New hexcode target is", new_hexcode)
                    # print("\t    Searching at depth", new_depth)
                    # print("\t    Excluding", exclude_list)

                    tmp_str = str(i) + self.index_finder(
                        sequence=sequence,
                        hexcode=new_hexcode,
                        row=new_row,
                        index=i,
                        prev_index=i,
                        depth=new_depth,
                        exclude_list=exclude_list,
                    )

                    if tmp_str[-1] != "-":
                        return tmp_str

        return "-"

    #############################################
    # Wrapper function for index_finder
    def breach_protocol(self):

        # Takes sequences, generates all possible combinatinos
        # 	sequences, and iterates through them with index_finder.
        # 	Returns possible path answers

        answers = []
        sequence_strings = list(map("".join, self.SEQUENCES))

        # number of sequence we want to upload
        num_seq_codes = len(sequence_strings)
        target_seq_length = len("".join(sequence_strings))

        # if buffer is not large enough,
        # 	drops all codes to see which string is the longest (best)
        # 	assuming longest codes are at bottom (they are).
        # 	The bottom codes get dropped first, ensuring best outcome
        # 	Iterates until sequence length fits in buffer
        while target_seq_length > (2 * self.BUFFER_SIZE):

            best_seq_options = []

            # get all seq options when dropping one
            for i in range(num_seq_codes):
                best_seq_options.append(
                    sequence_strings[:i] + sequence_strings[i + 1 :]
                )

            # get index of longest sequence
            best_index = best_seq_options.index(
                max(best_seq_options, key=lambda x: len("".join(x)))
            )

            # update sequence strings and relevent variables
            sequence_strings = best_seq_options[best_index]
            num_seq_codes = len(sequence_strings)
            target_seq_length = len("".join(sequence_strings))

        # get all possible string combintations
        possible_sequences = [
            "".join(s)
            for s in list(itertools.permutations(sequence_strings, num_seq_codes))
        ]

        # iterate through possible paths and check them
        for seq in possible_sequences:

            # split sequence string into list
            list_seq = [seq[i : i + 2] for i in range(0, len(seq), 2)]
            hexcode = list_seq[0]

            # find indicies
            print("  //BREACHING SEQUENCE: " + str(list_seq))
            result = self.index_finder(
                sequence=list_seq,
                hexcode=hexcode,
                row=True,
                index=0,
                prev_index=0,
                depth=0,
                exclude_list=[],
            )

            # if solution found, format path as coordinates
            if result[-1] == "+":

                msg.print_pass(
                    "  //BREACHING_STATUS....................................................COMPLETE"
                )

                # formate path outputs and append to answers tab
                path = "['0" + result[0] + "', "
                for i in range(1, len(result) - 1):

                    if i % 2:
                        path += "'" + result[i] + result[i - 1] + "', "
                    else:
                        path += "'" + result[i - 1] + result[i] + "', "

                answers.append([str(list_seq), path[:-2] + "]"])

            else:
                msg.print_fail(
                    "  //BREACHING_STATUS......................................................FAILED"
                )

        msg.print_info("[ ALL SEQUENCE UPLOADS TESTED ]")

        return answers
