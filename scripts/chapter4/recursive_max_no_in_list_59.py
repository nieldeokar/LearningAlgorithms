

def maxInList(arr):
	x = 0
	if(len(arr) == 0 ):
		return 0
	elif arr[0] < maxInList(arr[1:]) :
		x = 
		arr[0] = maxInList(arr[1:])


print maxInList([4,2,3,5])