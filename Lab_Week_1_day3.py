'''Lab_Week1_Day 3_12_19_2024_8506
Assignment Questions:

1. Using input() function take one number from the user and using ternary operators
check whether the number is even or odd'''

# input number from user.
number = int(input("Enter any positive integer: "))

# checking whether the input number is even or odd using ternary operators.
result = "Even" if number % 2 ==0 else "Odd"

# printing the result
print(f"The entered nummber is an {result} number")

'''2. Using input function take two number and then swap the number'''

#input two numbers from user.
print("Enter a number")
number1 = int(input("number1: "))
print("Enter another number")
number2 = int(input("number2: "))

# swapping the numbers.
number1, number2 = number2, number1

# printing the swapped numbers.
print(f"Swapped numbers: \nnumber1 = {number1}\nnumber2 = {number2}")
