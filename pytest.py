'''Print args
'''
import argparse
import sys

def main(args):
	p = argparse.ArgumentParser(
		description=__doc__
	)
	p.add_argument(
		'msgs',
		action='store',
		nargs='*',
		help='msgs to print'
	)
	
	ns = p.parse_args(args)
	
	for msg in ns.msgs:
		print(msg)
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
