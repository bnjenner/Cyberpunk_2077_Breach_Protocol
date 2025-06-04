#!/usr/bin/env python3

import sys
from utils.cybermessages import CyberMessages as msg
from utils.sequences import SequenceHack
from utils.utils import read_csv

##########################################################################################
"""
BEACH ACCESS POINTS IN CYBERPUNK 2077

RULES:
	Traverse rows and columns to find path fulfilling all 
		hexcodes in sequences in their respective orders.
			0. Assumes all matricies are solvable.
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
"""


##########################################################################################
# Global Variables

# Found from: https://emojicombos.com/cyberpunk-2077-ascii-art
UNNECESSARY_INTRO = """////////////////////////////////////////////////////////////////////////////////

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⡔⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢚⣉⣠⡽⠂⠀⠀⠀⠀⡰⢋⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢴⡆⠀⠀
⠀⠀⠀⠀⠀⢀⡤⠐⢊⣥⠶⠛⠁⢀⠄⡆⣠⠤⣤⠞⢠⠿⢥⡤⠀⠀⠠⢤⠀⠀⠀⠤⠤⠤⡄⢠⠤⠄⠤⠀⠀⠒⣆⡜⣿⣄⠀⡤⢤⠖⣠⣀⠤⢒⣭⠶⠛⠃⠀⠀
⢀⣀⡠⢴⣎⣥⣴⣾⣟⡓⠒⠒⠒⠺⣄⡋⢀⡾⢃⣴⢖⣢⣞⢁⣋⣉⣹⠏⠚⠛⢛⣉⣤⡴⢞⠃⣰⠾⠟⣛⣩⢵⢶⡟⣰⠇⠘⡼⢡⡟⣀⡋⢵⡞⠋⠁⠀⠀⠀⠀⠀
⠈⠢⠄⠤⠤⠤⠤⠤⠴⠤⠴⠶⠶⢾⠟⣱⡿⢤⢿⣕⠾⣿⣿⣩⡭⢤⠞⣰⠶⢤⣀⡉⠓⢾⡍⣠⠴⠾⠛⠹⠡⣟⡁⢰⢏⣼⡇⢰⣿⢀⠟⠳⣤⣌⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢃⡼⠋⠛⠾⠚⠁⠀⠈⠉⠀⠀⠸⣄⠏⠀⠀⠈⠙⠓⡟⣰⠏⠀⠀⠀⠘⠾⠛⠳⠞⠉⠁⠙⠋⠙⠚⠀⠀⠀⠙⠛⢿⣷⣤⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣜⡵⠟⠀⠀⠀⠀⠀⠀⣼⣿⣾⣿⣽⣽⣿⣿⢏⢫⣻⡹⡽⣰⢏⣯⠍⡭⡍⣭⢩⡭⢩⡍⡏⡏⣯⡍⣍⠙⡭⢹⣄⣤⠄⢠⠉⠓⢿⣕⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣯⠃⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣽⣾⣾⣟⣯⣣⣱⣾⣟⣞⣸⣇⣳⣃⣿⣛⣷⣬⠧⠳⠇⠿⢧⢿⢀⣷⢸⠧⢾⢃⠇⠀⠀⠀⠀⠁


////////////////////////////////////////////////////////////////////////////////"""

# Read Sequences
SEQUENCES = read_csv(sys.argv[1])
FRAME = read_csv(sys.argv[2])

# Size of castable sequence
BUFFER_SIZE = int(sys.argv[3])

ERROR_CAP = BUFFER_SIZE - sum(map(len, SEQUENCES))


##########################################################################################
# main function
def main():

    # Print intro
    msg.print_warn(UNNECESSARY_INTRO)
    msg.print_info("[ ENGAGING BREACH PROTOCOL... ]")

    # Find breach solutions
    SeqHack = SequenceHack(FRAME, SEQUENCES, BUFFER_SIZE)
    solutions = SeqHack.breach_protocol()

    # check if solutions
    if len(solutions) == 0:

        # print failure message
        msg.print_fail("[ NO SUCCESSFUL SOLUTIONS IDENTIFIED ]")
        msg.print_fail("  //ROOT_ATTEMPT_1")
        msg.print_fail("  //ROOT_ATTEMPT_2")
        msg.print_fail("  //ROOT_ATTEMPT_3")
        msg.print_fail("  //ROOT_FAILED")
        msg.print_fail("  //ROOT_REBOOT")
        msg.print_fail(
            "  //ACCESSING.............................................................FAILED"
        )
        msg.print_fail(
            "  //ACCESSING.............................................................FAILED"
        )
        msg.print_fail(
            "  //ACCESSING.............................................................FAILED"
        )
        msg.print_fail(
            "  //ACCESSING.............................................................FAILED"
        )
        msg.print_fail(
            "  //ACCESSING.............................................................FAILED"
        )
        msg.print_fail("[ USER TERMINATED PROCESS ]")
        msg.print_fail("[ BREACH ATTEMPT FAILED ]")

    else:

        # print success message
        msg.print_pass("[ SUCCESSFUL SEQUENCES IDENTIFIED ]")
        msg.print_pass("  //ROOT")
        msg.print_pass("  //ACCESS_REQUEST")
        msg.print_pass("  //ACCESS_REQUEST_SUCCESS")
        msg.print_pass(
            "  //COLLECTING PACKET_1.................................................COMPLETE"
        )
        msg.print_pass(
            "  //COLLECTING PACKET_2.................................................COMPLETE"
        )
        msg.print_pass(
            "  //COLLECTING PACKET_3.................................................COMPLETE"
        )
        msg.print_pass(
            "  //COLLECTING PACKET_4.................................................COMPLETE"
        )
        msg.print_pass("  //LOGIN")
        msg.print_pass("  //LOGIN_SUCCESS")
        msg.print_pass("  //")
        msg.print_pass("  //UPLOAD_IN_PROGRESS")
        msg.print_pass("  //UPLOAD_COMPLETE!")
        msg.print_pass("[ ALL DAEMONS UPLOADED ]")
        msg.print_pass("[ SUCCESSFUL SEQUENCE UPLOADS: " + str(len(solutions)) + " ]")

        # print solutions
        solution_index = 0
        for path in solutions:
            msg.print_pass("  //INPUT_" + str(solution_index) + "")
            msg.print_result("  //SEQUENCE:         ", path[0])
            msg.print_result("  //COORDINATES:      ", path[1])
            solution_index += 1

    # say goodbye
    msg.print_info("[ BREACHING PROCESS COMPLETE ]")
    msg.print_info("[ EXITING INTERFACE ]")
    msg.print_warn(
        "////////////////////////////////////////////////////////////////////////////////"
    )


if __name__ == "__main__":
    main()
