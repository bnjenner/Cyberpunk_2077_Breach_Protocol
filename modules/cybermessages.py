import sys

##########################################################################################

class CyberMessages():

	# This set of functions is completely unnecessary, but cool for the cyberpunk vibe
	#	Modified from this forum response: https://stackoverflow.com/questions/39473297/how-do-i-print-colored-output-with-python-3
	
	def print_fail(message, end = '\n'):
		sys.stderr.write('\x1b[1;31m' + message + '\x1b[0m' + end)

	def print_pass(message, end = '\n'):
		sys.stdout.write('\x1b[1;32m' + message + '\x1b[0m' + end)

	def print_warn(message, end = '\n'):
		print('\033[93m{}\033[1m'.format(message))

	def print_info(message, end = '\n'):
		sys.stdout.write('\x1b[1;34m' + message + '\x1b[0m' + end)

	def print_result(message, code, end = '\n'):
		sys.stdout.write(message + '\x1b[1;33m' + code + '\x1b[0m' + end)
