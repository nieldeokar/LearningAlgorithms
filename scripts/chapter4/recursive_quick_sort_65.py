# Doing quick Sort




def quicksort(array):
	if len(array) < 2:
		return array # Base case: arrays with 0 or 1 element are already sorted
	else:
		pivot = array[0] # Recursive case
		less = [i for i in array[1:] if i <= pivot]      #   Sub-array of all the elements less than the pivot
		greater = [i for i in array[1:] if i > pivot]  # Sub-array of all the elements greater than the pivot
   		return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([10, 5, 2, 3])