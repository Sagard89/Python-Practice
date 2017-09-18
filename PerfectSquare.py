import math
 
# get user input
user_number = input("Enter a number to see if it's a perfect square: ")
 
# define function and calculate
def perfect_square(user_number):
    root = math.sqrt(int(user_number))
    return int(root) ** 2 == int(user_number)
 
# loop through conditions and output suites
while not perfect_square(user_number):
    user_number = input("The number " + str(user_number) + " is 'not' a perfect square. Try again: ")
else:
    print("\nThe number " + str(user_number) + " is a perfect square! Good job!")