[2, 1, 3, 4, 5, 6, 7, 8, 4]


def quicksort(array, lowIn, highIn):
	if (highIn - lowIn) > 0:
		p = partition(array, lowIn, highIn)

		quicksort(array, lowIn, p-1)
		quicksort(array, p+1, highIn)

def partition(array, lowIn, highIn):
	pivot = highIn
	div = lowIn

	for i in range(lowIn, highIn):
		if array[i] < array[pivot]:
			array[i], array[div] = array[div], array[i]
			div += 1

	array[div], array[pivot] = array[pivot], array[div]
	return div


A = [2, 1, 3, 4, 5, 6, 7, 8, 4]
B = [3, 65, 767, 12, 43, 1, 4, 5, 4, 6]
print(B)
quicksort(B, 0, 9)
print(B)