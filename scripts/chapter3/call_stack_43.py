import sys


def greet(name):
	print 'hello, ' + name + '!' 
	greet2(name)
	print "getting ready to say bye..."
	bye()

def greet2(name):
	print "How are you "+ name + "?"


def bye():
	print "ok bye!"


if len(sys.argv[1:]) > 0 :
	greet(sys.argv[1])
else :
	greet('Nilesh')