import random
while(True):
    chips = 100
    print("You have five Rolls to make your point\n")
    print("Your bet cannot exceed the amount you have left in your bank.\n")
    print("You have " + str(chips) + " chips in your bank.")
    # getting the bet input from user
    bet = int(input("Place your bet: "))
    # getting the point input from user
    point = int(input("What is your point?: "))
    i = 1
    win = 0
    roll_count = 5
    while (roll_count > 0):
        print("\nYou have "+str(roll_count)+" more rolls to make your point.\n")
        print("Rolling the dice...\n\n")
        print("Roll number "+str(i)+" of 5")
        print("The Values are: ")
        # rolling die1 and die2 using random module to random number between 1 to 6
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1)
        print(die2)
        print("\nYou rolled "+ str(die1+die2))
        print("Your point is "+str(point))
        # if die value not equal to point repeat again until count goes to zero
        if (die1 + die2 != point):
            print("You did not make your point")
            i += 1
            roll_count -= 1
        else:
            print("Congrats! You made your point")
            win = 1
            print("Your bet is doubled \n")
            chips = chips + bet * 2
            print("The value of your chips in bank is: " + str(chips))
            break
    if (win == 0):
        print("Sorry, you lost your bet. -" + bet + "\n")
        chips = chips - bet
        print("The value of your chips in bank is: " + str(chips))
        print("Roll the dice 5 times again? (yes/no): ")
        play = input()
        if (play != 'yes'):
            break
    if (win == 1):
        print("Roll the dice 5 times again? (yes/no): ")
        play = input()
        if (play != 'yes'):
            break