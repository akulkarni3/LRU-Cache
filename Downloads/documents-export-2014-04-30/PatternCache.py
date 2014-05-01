#!usr/bin/python

from sys import argv
from llist import dllist, dllistnode
import pdb

hits = 0
misses = 0
log_count = 0
reboots = 0

class LruCache(object):

    def checkfull(self, app_launched):
    	global reboots
        if dlist.size < maxsize:
	   dlist.appendleft(app_launched)
	   return None
	else:
	   for past_app_launched in historylist:
	       if past_app_launched == app_launched:
	            reboots +=1
		    break
	   dlist.popright()
           dlist.appendleft(app_launched)
	   return None


    def autofull(self,app_launched):
    	global reboots
        for past_app_launched in historylist:
	   if past_app_launched == app_launched:
	       reboots +=1
	       break
        if dlist.size == maxsize:
	   dlist.popright()
	
	return None
   

    def autoexists(self, app_launched, i, temp):
	global hits
	global misses
	global array
	global breakpoints
	k = 0
	while k < breakpoints[i]:
	    count = 0
	    for app in dlist:
	        count+= 1 
                if array[temp+breakpoints[i]-1-k] == app:
		    if k == breakpoints[i]-1:
	    	        hits+= 1
	            if app != dlist[0]:
		        node = dlist.nodeat(count-1)
	                dlist.remove(node)
		        dlist.appendleft(array[temp+breakpoints[i]-1-k])
		        break		    
                else:
	            if count == dlist.size:
	                lru.autofull(app_launched)
			dlist.appendleft(array[temp+breakpoints[i]-1-k])
			if k == breakpoints[i]-1:
		             misses += 1
		        break
	    k += 1		

 

    def alreadyexists(self, app_launched):
        count = 0
	global hits
	global misses
	for app in dlist:
	    count+= 1 
            if app_launched == app:
	    	hits+= 1
	        if app != dlist[0]:
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
	    return None
	else:
            lru.alreadyexists(app_launched)



    def autoemptycheck(self, app_launched,i,temp):
    	global misses
	global breakpoints

    	if dlist.size == 0:
             k = 0
             while k < breakpoints[i]:
	        dlist.appendleft(array[temp+breakpoints[i]-1-k])
                k += 1
	     misses += 1
	     return None
	else:
             lru.autoexists(app_launched, i, temp)



    def patternscheck(self,app_launched):
        '''Checking if there is pattern'''
	global breakpoints
	global array
	global i

	index = 0
	i = 0
	for traverse in breakpoints:
	     index = index + traverse
	     temp = index - traverse
	     if app_launched == array[temp]:
		  lru.autoemptycheck(app_launched, i, temp)
		  return True
             i += 1
	    


    def pushapplications(self, maxsize, logs):
    	global log_count
	global hits
    	for app_launched in logs:
	    log_count += 1
	    if log_count == 50 or log_count == 100 or log_count == 200 or log_count == 300 or log_count == 400:
	    	 print '-' * 80
	         print 'Processed logs = ',log_count,' Hits = ',hits ,' Misses = ', misses
	     
	    if dlist.size != 0 and app_launched == dlist[0]:
		 hits += 1
	    else:
	         if not lru.patternscheck(app_launched):
	    	      '''Not a pattern--> LRU Caching'''
	              lru.checkempty(app_launched)
	    
	    historylist.appendleft(app_launched)
    

    
    def readinglogs(self, maxsize, filename):
        '''Reading the log file'''
        txt = open(filename)
        print "The log file used is %r: " % filename
	global logs
        logs = [line.strip() for line in open(filename)]
	lru.pushapplications(maxsize,logs)



    def getpatterns(self):
         '''Get Patterns from User'''
	 global breakpoints
	 global array

	 patterns = int(raw_input('How many patterns are to be inserted ? Preferably less than three \n'))
	 print "Enter size of ALL Patterns starting from first to last seperated by space "
	 patternsize =  raw_input()
	 breakpoints = map(int,patternsize.split())
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
    maxsize = 15
    lru.readinglogs(maxsize, filename)
    print '#' * 80
    print 'Final Contents of Stack   => \n',dlist
    print 'Stack Size                = ',dlist.size
    print 'Total hits                = ', hits
    print 'Total misses              = ', misses
    print 'Total Application Reboots = ', reboots
    print '#' * 80

