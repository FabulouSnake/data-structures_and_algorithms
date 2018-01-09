a = 5
b = 4

# prints the 'value' number both in Decimal and Binary notation
def printDecAndBin(value):
	print("Decimal: {:d} \nBinary: {:b}".format(value, value))
	print("---------------")

# printing the numbers a, b in binary
print("A: ")
printDecAndBin(a)
print("B: ")
printDecAndBin(b)

# AND
print("AND: ")

andValue = a & b
printDecAndBin(andValue)

# OR
print("OR: ")


orValue = a | b
printDecAndBin(orValue)

# XOR
print("XOR: ")
xorValue = a ^ b
printDecAndBin(xorValue)

# Shifting bits to the left
print("Shifting bits to the left (2 places)")

shiftLeft = b << 2



print("BEFORE: ")
printDecAndBin(b)
print("AFTER: ")
printDecAndBin(shiftLeft)



# Shifting bits to the right
print("Shifting bits to the right (2 places)")

shiftRight = b >> 2



print("BEFORE: ")
printDecAndBin(b)
print("AFTER: ")
printDecAndBin(shiftRight)

# Complement
print("Complement: ")
print("A: ")
printDecAndBin(a)
print("Complement of A (Negative A): ")
complOfA = ~ a
printDecAndBin(complOfA)





