# Exercise 4.1 
# Print the sum of an array using recursive funtion :
# 
# Same can be done by loop in this way :
# 
# def sum(arr): 
# 	total = 0
# 	for x in arr:
# 		total += x 
# 	return total


def sum(arr):
	
	if(len(arr) == 0):
		return 0
	elif len(arr) == 1:
		return arr[0]
	else :
		return arr[0] + sum(arr[1:])


print sum([2,4,6])