
# 4.2 Write a recursive function to count the number of items in a list.
# Below mentioned function will count the number of the elements in the list recursively.




def count(arr):
	if(len(arr) == 0): # Base case
		return 0
	else: # Recursive case
		return 1 + count(arr[1:])



print count([1,2,3,4,5])