'''Lab_Week 1_Day 2_12_18_2024

Problem 1:
Write a program to input 3 sides of a triangle
and calculate and print its area.'''

# Input lengths of the sides of the triangle
side1 = float(input("Enter length of 1st side of the triangle: "))
side2 = float(input("Enter length of 2nd side of the triangle: "))
side3 = float(input("Enter length of 3rd side of the triangle: "))

# Calculate the semi-perimeter
s = (side1 + side2 + side3) / 2

# Calculate the area using Heron's formula
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

# Print the area of the triangle
print(f"Area of the triangle: {area:.2f}")


'''Problem 2:
Write a program to input the temperature in Celsius
and calculate ans print it in Fahrenheit.'''

# input the temperature in Celsius.
celsius = float(input("Enter the temperature in Celsius: "))

# conversion of Celsius into Fahrenheit.
fahrenheit = (celsius * (9/5))+32

# print the temperature in Fahrenheit.
print(f"The temperature in Fahrenheit is {fahrenheit: .2f}")