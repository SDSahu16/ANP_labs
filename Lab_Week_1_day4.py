# # Day-4 Lab
# # Lab_Week 1_Day 12_20_2024
# #
# # Assignment:
# # 1. Python Program to Find the Largest Among Three Numbers (Using nested if)
#
# Input the first number
num1 = int(input("Enter 1st number: "))

# Input the second number
num2 = int(input("Enter 2nd number: "))

# Input the third number
num3 = int(input("Enter 3rd number: "))

# Compare the first number with the second number
if num1 > num2:
    # If the first number is greater than the second, compare it with the third number
    if num1 > num3:
        # If the first number is also greater than the third, it is the largest
        print(f"The 1st number: {num1} is the greatest among the three numbers {num1, num2, num3}.")
    else:
        # If the third number is greater than the first, it is the largest
        print(f"The 3rd number: {num3} is the greatest among the three numbers {num1, num2, num3}.")
else:
    # If the second number is greater than or equal to the first, compare it with the third number
    if num2 > num3:
        # If the second number is greater than the third, it is the largest
        print(f"The 2nd number: {num2} is the greatest among the three numbers {num1, num2, num3}.")
    else:
        # If the third number is greater than the second, it is the largest
        print(f"The 3rd number: {num3} is the greatest among the three numbers {num1, num2, num3}.")

#
#
# # 2. A transport company charges the fare according to following table:
# # Distance Charges
# # 1-50 	8 Rs./Km
# # 51-100 	10 Rs./Km
# # > 100 	12 Rs/Km
# #
# # Write a program to input distance travelled as input and calculate and print the total charge.
# # Use comments where necessary and follow python naming conventions.
#

# Taking the distance travelled as input from user
distance = int(input("Enter the Distance travelled (in Kms): "))

# checking whether the distance is in between 1-50Kms
if distance in range(1,51):
    # if total distance is in between 1-50Kms then printing the total charge as 8 times the total distance
    print(f"Total charge is Rs. {distance * 8}")
# checking whether the distance is in between 51-100Kms
elif distance in range(51,101):
    #if total distance is in between 51-100Kms then printing the total charge as 10 times the total distance
    print(f"Total charge is Rs. {distance * 10}")
else:
    # if total distance is greater than 100Kms then printing the total charge as 12 times the total distance
    print(f"Total charge is Rs. {distance * 12}")