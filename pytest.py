'''Print args
'''
import argparse
import sys

p = argparse.ArgumentParser(
	description=__doc__
)
p.add_argument(
	'msgs',
	action='store',
	nargs='*',
	help='msgs to print'
)

ns = p.parse_args(sys.argv[1:])

for msg in ns.msgs:
  print(msg)

sys.exit(0)
