#!/usr/bin/python
import calendar
import cmath,time


print cmath.sqrt(16)

string1 = 'sddff'
tuple1 = ('a','b')

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Alice']: ", dict['Name']
print len(dict)
print str(dict)
print type(tuple1)
print dict.values()
print dict.keys()

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks
print calendar.isleap(2016)
print calendar.calendar(2018,w=2,l=1,c=7)

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme( str = "My string")