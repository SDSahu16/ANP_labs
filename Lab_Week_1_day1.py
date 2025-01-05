'''Lab_8506_week 1_day 1_12_17_2024

Problem 1 :
 Write a program to take the diamater of a circle as user input
 and calculate and print its area & circumference.'''

diameter = float(input("Enter the Diameter: "))
area = 3.14*pow(diameter/2,2)
circumference = 2*3.14*(diameter/2)
print("Area: ", round(area, 2))
print("Circumference: ", round(circumference, 2))
