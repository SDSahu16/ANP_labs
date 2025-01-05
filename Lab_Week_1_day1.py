'''Lab_8506_week 1_day 1_12_17_2024

Problem 1 :
 Write a program to take the diamater of a circle as user input
 and calculate and print its area & circumference.'''

# input diameter of the circle.
diameter = float(input("Enter the Diameter: "))

# calculate the area of the circle.
area = 3.14*pow(diameter/2,2)

# calculate the circumference of the circle.
circumference = 2*3.14*(diameter/2)

# print the area of the circle.
print("Area: ", round(area, 2))

# print the circumference of the circle rounded upto 2 decimal places.
print("Circumference: ", round(circumference, 2))
