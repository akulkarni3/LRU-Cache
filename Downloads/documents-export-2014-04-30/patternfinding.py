from sys import argv
from llist import dllist, dllistnode

script, filename = argv
txt = open (filename)
logs = [line.strip() for line in open(filename)]
withoutduplicates = set(logs)

def contains(logs, filter):
    for x in logs:
        if filter(x):
	    return True
    return False

for everyapp in withoutduplicates:
    print everyapp
    hits = 0
    i = 0
    while i < len(logs)-14:
         position = 0
         for item in logs[i:i+14]:
	      if everyapp == item:
	           for app in withoutduplicates[position,len(withoutduplicates)]:
	               matching = [app for app in withoutduplicates if app in s]
		   
	 i +=1
	 position +=1

		   
