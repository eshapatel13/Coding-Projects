import math

while True:
    # menu options
    print("Possible operations.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Average")
    print("5. Square Root")

    # prompting for user choice
    choice = input("Enter your desired operation (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        # addition WORKS
        if choice == '1':
            sum = 0.0
            number = 1
            print("Input some number to get their average. Input 0 to finish: ")
            while number != 0:
                number = int(input(""))
                sum = sum + number
            print("The sum is: ", sum)
        # subtraction
        elif choice == '2':
            difference = 0.0
            sum = 0.0
            number = 1
            large_num = int(input("Input the number you'd like to subtract from: "))
            print("Input some numbers to subtract from ", large_num, ". Input 0 to finish: ")
            while number != 0:
                number = int(input(""))
                sum = sum + number
            difference = large_num - sum
            print("The difference is: ", difference)
        # multiplication
        elif choice == '3':
            lst = []
            n = int(input("Enter the amount of numbers you'd like to multiply: "))
            n += 1
            print("Input some numbers to get their product. Input 0 to finish: ")
            for i in range(0, n):
                ele = int(input(""))
                lst.append(ele)
            lst.pop()
            product = 1.0
            for x in lst:
                product = product * x
            print("The product is: ", product)
        # average WORKS
        elif choice == '4':
            count = 0
            sum = 0.0
            number = 1
            print("Input some number to get their average. Input 0 to finish: ")
            while number != 0:
                number = int(input(""))
                sum = sum + number
                count += 1
            average = sum / (count - 1)
            print("The average is: ", average)
        # square root WORKS
        elif choice == '5':
            print("Enter the number you'd like the square root of: ")
            number = int(input(""))
            square_root = math.sqrt(number)
            print("The square root is: ", square_root)
        # asking user if they'd like to quit
        # break loop if user enters q
        next_calc = input("Enter q to quit, or yes for another calculation: ")
        if next_calc == 'q':
            break
    else:
        print("Invalid output.")

'''
product = 1.0
number = 1
print("Input some numbers to get their product. Input 0 to finish: ")
while number != 0:
    number = int(input(""))
    product = product * number
print("The product is: ", product)
'''