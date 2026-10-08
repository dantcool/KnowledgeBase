# Step 1: Input handling for non-integers
num = input("Enter Number between 1 and 111\n")

try:
    num = int(num)
except ValueError:
    num = 0

# Step 2: Input handling for values > 111 using division by zero
try:
    if num > 111:
        1 / 0
except ZeroDivisionError:
    num = 1

# Step 3: Main logic OUTSIDE of try-except blocks
if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
    print(f"You entered {num} and its a prime number!!")
elif num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
    print("You must have entered 105!")
elif num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print("OH STOP NOW")
else:
    print("Oh I see, your number must be a multiple of 4, if not a 0!!")