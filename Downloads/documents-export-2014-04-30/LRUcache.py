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
 

    def pushapplications(self, maxsize, logs):
    	global log_count
	global hits
        global reboots
    	for app_launched in logs:
	    log_count+= 1
	    if log_count == 100 or log_count == 200 or log_count == 300 or log_count == 400 or log_count == 50:
	    	 print '-' * 80
	         print 'Processed logs = ',log_count,' Hits = ',hits ,' Misses = ', misses,' Reboots = ',reboots
	    if dlist.size != 0 and app_launched == dlist[0]:
	    	 hits += 1
	   #     print "Both are same apps "+ app_launched +" and  "+ dlist[0]
	    else:
	         lru.checkempty(app_launched)
	    
	    historylist.appendleft(app_launched)
    
    
    def readinglogs(self, maxsize, filename):
        '''Reading the log file'''
        txt = open(filename)
        print "The log file used is %r: " % filename
	global logs
        logs = [line.strip() for line in open(filename)]
       # print '\n'.join(logs)
	lru.pushapplications(maxsize,logs)

	
if __name__ == "__main__":
    lru = LruCache()
    dlist = dllist()
    historylist = dllist()
    script, filename = argv
    maxsize = 15
    lru.readinglogs(maxsize, filename)
    print '#' * 80
    print 'Final Contents of Stack   => \n',dlist
    print 'Stack Size                = ',dlist.size
    print 'Total hits                = ', hits
    print 'Total misses              = ', misses
    print 'Total Application Reboots = ', reboots
    print '#' * 80
