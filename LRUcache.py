#!usr/bin/python

from sys import argv
from llist import dllist, dllistnode
import pdb

hits = 0
misses = 0

class LruCache(object):

    def checkfull(self, app_launched):
        if dlist.size < maxsize:
	   print 'available slots '+ app_launched
	   dlist.appendleft(app_launched)
	   return None
	else:
	   dlist.popright()
	   print 'max reached '+ app_launched
           dlist.appendleft(app_launched)
	   return None
    
		     

    def alreadyexists(self, app_launched):
        count = 0
	global hits
	global misses
	for app in dlist:
	    count+= 1 
            if app_launched == app:
	    	hits+= 1
	        if app != dlist[0]:
	            print 'its a match '+ app
		    node = dlist.nodeat(count-1)
	            dlist.remove(node)
		    dlist.appendleft(app_launched)
		    return None
		    
            else:
	        if count == dlist.size:
	             lru.checkfull(app_launched)
		     misses += 1
		     return None


    def checkempty(self, app_launched):
    	global misses
    	if dlist.size == 0:
            dlist.appendleft(app_launched)
	    misses += 1
	    print "Application appended is " + app_launched
	    return None
	else:
            lru.alreadyexists(app_launched)
 

    def pushapplications(self, maxsize, logs):
    	for app_launched in logs:
	    if dlist.size != 0 and app_launched == dlist[0]:
	         global hits
	    	 hits += 1
	         print "Both are same apps "+ app_launched +" and  "+ dlist[0]
	    else:
	         lru.checkempty(app_launched)
    
    
    def readinglogs(self, maxsize, filename):
        '''Reading the log file'''
        txt = open(filename)
        print "Here is your file %r: " % filename
	global logs
        logs = [line.strip() for line in open(filename)]
       # print '\n'.join(logs)
	lru.pushapplications(maxsize,logs)

	
if __name__ == "__main__":
    lru = LruCache()
    dlist = dllist()
    script, filename = argv
    maxsize =16
    lru.readinglogs(maxsize, filename)
    print dlist
    print dlist.size
    print 'hits = ', hits
    print 'misses = ', misses


