# equation is P' = P(1 + (r/n))**nt
# P is the initial amount of investment
# r is interest rate
# n is number of compounding per year (eg. 12-monthly, 4-quarterly, 1-annual)
# t is number of years of interest
# P' is the new balance of the account after earning for t years

# write a program to gather these variables and calculate some figures

print("Welcome to the Compound Interest Calculator")

# get input for initial amount
# convert to float
initial_amount = float(input("Please enter the initial amount of your investment: "))

# get input for initial amount
# convert to float
interest_rate = float(input("Please enter the interest rate (e.g., '.03' for 3% interest): "))

# get input for initial amount
# convert to int
time = float(input("Please enter the number of years for the investment: "))

# get input for initial amount
# convert to int
compounding = float(input("Please enter the number of compoundings per year: "))

# calculate by pieces
# calculate r/n
rate_compounding = interest_rate / compounding
# add 1 to r/n
rate_compounding += 1
# calculate nt
compounding_time = compounding * time
# finish calculation
new_amount = initial_amount * rate_compounding**compounding_time

# print original investment, interest earned, and the final balance
# use round to ensure 2 decimal places
print("Original Investment: $", format(initial_amount, ',.2f'), sep="")
print("Interest Earned: $", format((new_amount - initial_amount), ',.2f'), sep="")
print("Final Balance: $", format(new_amount, ',.2f'), sep="")
