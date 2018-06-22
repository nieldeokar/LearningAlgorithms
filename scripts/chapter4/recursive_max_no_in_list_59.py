# 4.3 Find the maximum number in a list.
# 



def maxInList(arr):
	if(len(arr) == 0): # Base case
		return 0
	elif len(arr) >= 2 : # Recursive case
		if arr[0] < arr[1]:
			arr[0] = arr[1]
		del arr[1]
		return maxInList(arr)
	else:
		return arr[0]

print maxInList([71,4,2,12,3,5,8])