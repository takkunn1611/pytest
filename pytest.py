'''
Print args.

Usage:
	pytest.py MSGS...
	pytest.py (-h | --help)
	
Options:
	-h	--help	show help
'''

from docopt import docopt
import sys

def main(argv):
	args = docopt(__doc__, argv=argv)
	
	for msg in args['MSGS']:
		print(msg)
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
