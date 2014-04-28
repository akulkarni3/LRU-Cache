#!usr/bin/python

from sys import argv
from llist import dllist, dllistnode
import pdb

hits = 0
misses = 0
log_count =0
reboots = 0

class LruCache(object):

    def checkfull(self, app_launched):
    	global reboots
        if dlist.size < maxsize:
#	   print 'available slots '+ app_launched
	   dlist.appendleft(app_launched)
	   return None
	else:
	   for past_app_launched in historylist:
	       if past_app_launched == app_launched:
#	            print 'rebooted application = '+ app_launched + past_app_launched
	            reboots +=1
		    break
	   dlist.popright()
#	   print 'max reached '+ app_launched
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
	 #          print 'its a match '+ app
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
	 #  print "Application appended is " + app_launched
	    return None
	else:
            lru.alreadyexists(app_launched)

     
    def patternscheck(self,app_launched):
        '''Checking if there is pattern'''
	global breakpoints
	global array
	index = 0
	for traverse in breakpoints:
	     index = index + traverse
	     temp = index - traverse
	     if app_launched == array[temp]:
	          print 'its a match at position i =', temp+1
#		  lru.automatedpush(app_launched)
		  return True

    def pushapplications(self, maxsize, logs):
    	global log_count
	global hits
    	for app_launched in logs:
	    log_count+= 1
	    if log_count == 5 or log_count == 10 or log_count == 15 or log_count == 20 or log_count == 25:
	    	 print '-' * 80
	         print 'Processed logs = ',log_count,' Hits = ',hits ,' Misses = ', misses
	     
	    if dlist.size != 0 and app_launched == dlist[0]:
		 hits += 1
	    else
	         if lru.patternscheck(app_launched):
	    	      '''Do something'''
	         else:
	              lru.checkempty(app_launched)
	    
	    historylist.appendleft(app_launched)
    

    
    def readinglogs(self, maxsize, filename):
        '''Reading the log file'''
        txt = open(filename)
        print "The log file used is %r: " % filename
	global logs
	global breakpoints
        logs = [line.strip() for line in open(filename)]
       # print '\n'.join(logs)
	lru.pushapplications(maxsize,logs)

    def getpatterns(self):
         '''Get Patterns from User'''
	 global breakpoints
	 global array

	 patterns = int(raw_input('How many patterns are to be inserted ? Preferably less than three \n'))
	 print "Enter size of ALL Patterns starting from first to last seperated by space "
	 patternsize =  raw_input()
	 breakpoints = map(int,patternsize.split())
	 breakpoints.insert(0,0)
	 print breakpoints
         print 'Print out Patterns seperated by a space'
         patternsize =  raw_input()
	 array = map(str,patternsize.split())
	 print array
	 return None


	
if __name__ == "__main__":
    lru = LruCache()
    dlist = dllist()
    historylist = dllist()
    script, filename = argv
    lru.getpatterns()
    maxsize = 16
    lru.readinglogs(maxsize, filename)
    print '#' * 80
    print 'Final Contents of Stack   => \n',dlist
    print 'Stack Size                = ',dlist.size
    print 'Total hits                = ', hits
    print 'Total misses              = ', misses
    print 'Total Application Reboots = ', reboots
    print '#' * 80

