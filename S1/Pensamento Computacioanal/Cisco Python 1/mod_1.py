# Notes of CISCO Python 1
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))

# Convert to string
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))


# Verify the type of data
var = input("Enter a number: ")
print(type(var)) # output: <class 'str'>