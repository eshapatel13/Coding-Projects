'''This program allows the user to enter a number and conduct the Babylonian method of finding the square root to then find the square root of that number.'''

# find the square root of a number using the babylonian method
# x is the number we're trying to find the square root of
# e is the estimate
# epsilon is 0.00001
# |x/e - e| < epsilon means that we have a good enough estimate
# (x/e + e)/2 is the new estimate
# use a while loop to repeat the process till we can find the square root

# set value of epsilon
epsilon = 0.0001
# get input from user
x = int(input("Enter a positive integer value: "))
# set e equal to x
e = float(x)
# while loop in order to perform the calculations and repeat them
while abs((x/e) - e) > epsilon:
    if x <= 0:
        print("Your number must be a positive integer. Please try again.")
        x = int(input("Enter a positive integer value: "))
        e = float(x)
    else:
        e = ((x / e) + e) / 2

# round e to 3 decimal places
e = format(e,'.3f')
# print the values
print("Value Square Root")
print(x,e,sep='     ')