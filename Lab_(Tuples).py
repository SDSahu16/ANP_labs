#Lab_Tuples_01_29_2025_8506
#Assignment:

'''1. Write a Python program to find the number of times 4 appears in the tuple.
Input:
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
Output: 3'''

# Given Tuple
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# Use the count() method to find how many times '4' appears in the tuple
print(f"Number of times 4 appeared in the tuple is : {tuplex.count(4)}")

'''2.Write a Python program to convert a list to a tuple.
Input: listx = [5, 10, 7, 4, 15, 3]
Output: (5, 10, 7, 4, 15, 3)'''

# Define a list containing some integers
listx = [5, 10, 7, 4, 15, 3]

# Convert the list to a tuple
tupled_list = tuple(listx)

# Print the converted tuple
print(f"The required tuple is: \n{tupled_list}")

# Print the type of the converted object to confirm it's a tuple
print(type(tupled_list))

'''3. Write a Python program to calculate the sum of the numbers in a given tuple.
Input: tuples_list = [(1, 2), (3, 4), (5, 6)]'''

tuples_list = [(1, 2), (3, 4), (5, 6)]

# Create an empty list to store the sum of numbers in each tuple
sum_list = []

# Iterate through each tuple in the list
for tups in tuples_list:
    # Calculate the sum of the current tuple and append it to the sum_list
    sum_list.append(sum(tups))

# Print the new list containing the sum of numbers in each tuple
print(f"New list containing Sum of numbers in the tuples in the given list: \n{sum_list}")

# Calculate and print the total sum of all the sums from the sum_list
print(f"Total sum = {sum(sum_list)}")

'''4.Write a python program and iterate the given tuples
Input:
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)'''

# Tuples containing employee details
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# List of all employee tuples
employees = [employee1, employee2, employee3]

# Iterate through each employee tuple
for employee in employees:
    # Unpack tuple into individual variables
    name, emp_id, department, salary = employee
    # Print employee details
    print(f"Employee Name: {name}")
    print(f"Employee ID: {emp_id}")
    print(f"Department: {department}")
    print(f"Salary: {salary}")
    print("-" * 30)  # Separator for readability
