from sys import argv
from llist import dllist, dllistnode

script, filename = argv
txt = open (filename)
logs = [line.strip() for line in open(filename)]

withoutduplicates = set(logs)

print '\n'.join(withoutduplicates)
