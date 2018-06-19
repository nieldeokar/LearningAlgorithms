import sys

# This function calculates the factorial of a number passed as command line arg.
# Funtion calls itself Recursively to calculate the factorial.

def fact(x):
	if x == 1:
		return 1
	else:
		return x * fact(x-1)


if len(sys.argv[1:]) > 0 :
	print fact(int(sys.argv[1]))
else:
	print fact(3)




#Suppose you accidentally write a recursive function that runs forever.
#As you saw, your computer allocates memory on the stack for each function call.
#What happens to the stack when your recursive function runs forever?
#
# Ans :
# We get - maximum recursion depth exceeded Error
# To test remove line 7,8,9 and run program. It will run infinitely
# default recursion limit is 1000
