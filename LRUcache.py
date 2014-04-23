#!usr/bin/python


from sys import argv
from llist import dllist, dllistnode
import pdb

class LruCache(object):

    
    def checkfull(self, app_launched):
        if dlist.size < maxsize:
	   print 'available slots '+ app_launched
	   dlist.appendleft(app_launched)
	   return None
	else:
	   dlist.popright()
	   print 'max reached'+ app_launched
           dlist.appendleft(app_launched)
	   return None
    
		     

    def alreadyexists(self, app_launched):
        count = 0
	for app in dlist:
	    count+= 1 
            if app_launched == app:
	        if app != dlist[0]:
	            print 'its a match '+ app
		    node = dlist.nodeat(count-1)
	            dlist.remove(node)
		    dlist.appendleft(app_launched)
		    return None
		  # print dlist
		    
            else:
	        if count == dlist.size:
	             lru.checkfull(app_launched)
		     return None


    def checkempty(self, app_launched):
    	if dlist.size == 0:
            dlist.appendleft(app_launched)
	    print "Application appended is " + app_launched 
	    return None
	else:
            lru.alreadyexists(app_launched)
 

    def pushapplications(self, maxsize, logs):
    	for app_launched in logs:
	    if dlist.size != 0 and app_launched == dlist[0]:
	         print "Both are same apps "+ app_launched +" and  "+ dlist[0]
	    else:
	         lru.checkempty(app_launched)
    
    
    def readinglogs(self, maxsize, filename):
        '''Reading the log file'''
        txt = open(filename)
        print "Here is your file %r: " % filename
        logs = [line.strip() for line in open(filename)]
       # print '\n'.join(logs)
       # dlist = dllist() 
	lru.pushapplications(maxsize,logs)

	
if __name__ == "__main__":
    lru = LruCache()
    dlist = dllist()
    script, filename = argv
    maxsize =16
    lru.readinglogs(maxsize, filename)
    print dlist
    print dlist.size






'''
#pushing applications to stack
for app_launch in logs:
    if app_launch != dlist.first:
    	print app_launch
	print dlist.first
        if dlist.size == 0:
            dlist.appendleft(app_launch)
	    print "Application appended"
	    print app_launch
        else:
	    count = 0
	    for app in dlist:
	    	count+= 1 
                if app_launch == app:
	            if app != dlist.first:
	                print 'its a match'
		        print app
		        print count
		        node = dlist.nodeat(count-1)
	                dlist.remove(node)
		        dlist.appendleft(app_launch)
		        print dlist
		    else:
		        if dlist.size < maxsize:
	       	            print 'available slots'
	        	    dlist.appendleft(app_launch)
	                else:
	                    dlist.popright()
	                    print 'max reached'
                            dlist.appendleft(app_launch)
   
    else:
    	print app_launch
    	print "Doing nothing. it was first element"
'''

