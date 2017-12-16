import math

def binary_search(seq, target):
	low = 0
	high = len(seq) - 1

	while low <= high:

		mid = low + (high - low) / 2

		mid = int(math.floor(mid))

		if (seq[mid] == target):
			return mid
		elif (seq[mid] < target):
			low = mid + 1
		else:
			high = mid - 1

A = [1, 3, 5, 7, 9, 11, 13, 14, 15, 16, 25, 43, 68, 71, 73, 75]
target = 68

target_index = binary_search(A, target)

print("Target: " + str(target))
print("Sequance: " + str(A))
print("Target_index: " + str(target_index))
print("Target in the array: " + str(A[target_index]))