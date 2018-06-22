
# 4.4 Remember binary search from chapter 1? 
# It is a divide-and-conquer algorithm, too. 
# Can you come up with the base case and recursive case for binary search?


# below coded example is a simple search
# Still need to find out something which will eliminate the 


guess = 4;

def binarySearch(arr):
	if(len(arr)==0):
		return 0
	elif guess < arr[len(arr)/2]:
		return binarySearch(arr[(len(arr)/2):])
	else:
		return binarySearch(arr[:(len(arr)/2)]) 


print binarySearch([1,2,3,4,5,6])

