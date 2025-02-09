#Day-13 Lab
#Assignment:

'''1. Write a Python program and calculate the mean of the below dictionary.
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
Output: 6.2'''

# Sample dictionary with integer values
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

try:
    # Get the mean of the values if the dictionary is not empty
    values = test_dict.values()
    mean = sum(values) / len(values) if values else 0

    # Print the mean, formatted to 2 decimal places
    print(f"The mean of the values is: {mean:.2f}")

# Handle errors if values are not numeric
except TypeError:
    print("Error: Dictionary contains non-numeric values.")

'''2.Write a Python script to concatenate the following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
merged_dict = {**dic1,**dic2,**dic3}
print(f"Concatenated Dictionary : {merged_dict}")

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

'''3.Write a Python program to get the key, value and item in a dictionary.
input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

# Sample dictionary with integer keys and values
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Print the table header
print("Key\tValue")
print("-" * 15)  # Print a line to separate the header from the data

# Iterate through each key-value pair in the dictionary
for key, value in dict_num.items():
    # Print each key and value separated by a tab
    print(f"{key}\t{value}")

'''4.Write a Python program to get the key, value and item in a dictionary.
Input: input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}
output:
Dictionary with empty items dropped:
{1: 10, 2: 20, 4: 40, 6: 60}'''

# Initialize the dictionary with keys and values
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

# Create an empty dictionary to store the filtered results
filtered_dict = {}

# Loop through each key-value pair in the original dictionary
for key, value in input_dict.items():
    # Only add the key-value pair to the filtered dictionary if the value is not None
    if value is not None:
        filtered_dict[key] = value

# Print the filtered dictionary
print("Dictionary with empty items dropped:")
print(filtered_dict)
