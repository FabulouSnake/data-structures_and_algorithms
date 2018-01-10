# prints the 'value' number both in Decimal and Binary notation
def printDecAndBin(value):
	print("Decimal: {:d} \nBinary: {:b}".format(value, value))
	print("---------------")


def countOneBits(num):
	numOfBits = 0
	while num:
		numOfBits += num & 1
		num >>= 1
	return numOfBits


a = 50
printDecAndBin(a)

print("One Bits: " + str(countOneBits(a)))


############################
## WORD PARITY ALGORITHMS ##
############################

# 1. Brute-force
def parityBruteForce(num):
	result = 0
	while num:
		result ^= num & 1
		num >>= 1
	return result

print(parityBruteForce(a))

# The complexity is O(n) where n is the size of the word,
# because we have to check every single bit



# 2. Removing the lowest 1-bit using x = x & (x -1)
def parityRemovingLowestOneBit(num):
	result = 0
	while num:
		printDecAndBin(num)
		result ^= 1

		# removes the lowest 1-bit in num
		num &= num -1 
	return result


print(parityUsingComplement(a))

# The complexity is O(k) where k is the number of 1-bits,
# because we need to make as many steps as there are 1-bits
# So we can just count the number of steps and if the number
# is odd the result is '1' and if it is even the result is '0'


def 


