import collections
from sys import argv
from llist import dllist, dllistnode

script, filename = argv
txt = open (filename)
logs = [line.strip() for line in open(filename)]

c = collections.Counter(logs)

for i,j in c.most_common():
    print "	 ",j,"		 ",i
