# # 1. Write a Python program to count the occurrences of each word in a
# # given sentence
# # string = “To change the overall look of your document. To change the look
# # available in the gallery”
#
sentence = "To change the overall look of your document . To change the look available in the gallery"

# Converting the string into a list of words
sentence_as_list = sentence.upper().split()

# Initialize an empty list to keep track of processed words
counter = []

# Using a for loop to iterate through each word in the list
for i in sentence_as_list:
    # Check if the current word has not already been processed
    if i not in counter:
        # If the word is not in the counter list, print the word and its count in the original list
        print(i.capitalize() + " =", sentence_as_list.count(i))
        # Add the word to the counter list to avoid processing it again
        counter.append(i)
#
#     # print(counter)
#
# #or another approach could be as follows:
# #
# Convert the string into a list of words
sentence_as_list = sentence.split()

# Initialize an empty dictionary to store word counts
word_count = {}

# Iterate through each word in the list
for word in sentence_as_list:
    # Check if the word is already in the dictionary
    if word in word_count:
        # If the word exists, increment its count by 1
        word_count[word] += 1
    else:
        # If the word does not exist, add it to the dictionary with a count of 1
        word_count[word] = 1

# Print each word and its count
for word, count in word_count.items():
    print(f"{word} = {count}")
#
#
# # 2. Write a Python program to remove a newline in Python
# # String = "\nBest \nDeeptech \nPython \nTraining\n"
line = "\nBest \nDeeptech \nPython \nTraining\n"

#replacing the new-line characters with empty string
new_line = line.replace("\n", "")

#printing the line without new-line characters
print(new_line)
#
# # 3. Write a Python program to reverse words in a string
# # String = “Deeptech Python Training”
# #
string = "Deeptech Python Training"

# Split the string into words, reverse the list, and join them with a space
reversed_words = " ".join((string.split())[::-1])

# Print the string with words in reversed order
print(reversed_words)
#
# #or we can use another approach without using join function and string slicer
#
# Initialize an empty string to store the result
flag = ""

# Split the input string into a list of words
string_list = string.split()

# Iterate through each word in the list
for i in string_list:
    # Check if the word is not already in the flag string
    if i not in flag:
        # Add the word to the beginning of the flag string
        flag = str(i) + " " + flag

# Print the final string with reversed word order
print(flag)
#
#
# # # 4. Write a Python program to count and display the vowels of a given text
# # # String=”Welcome to python Training
#
# Initialize the input string
text = "Welcome to python Training"

# Define a list of vowels
vowels = ["a", "e", "i", "o", "u"]

# Initialize an empty list to keep track of vowels already counted
vowel_counter = []

# Iterate through each character in the string
for i in text:
    # Check if the character is a vowel
    if i in vowels:
        # Ensure the vowel hasn't been counted already
        if i not in vowel_counter:
            # Print the count of the vowel in the text
            print(f"count of {i} is {text.count(i)}")
            # Add the vowel to the list of counted vowels
            vowel_counter.append(i)

#
#  #or using dictionary data structure
#
# Initialize an empty dictionary to store vowels and their counts
v = {}
# Iterate through each character in the string
for i in text:
    # Check if the character is a vowel
    if i in vowels:
        # If the vowel is already in the dictionary
        if i in v:
            # Increment its count by 1
            v[i] += 1
        # If the vowel is not in the dictionary
        else:
            # Add it to the dictionary with a count of 1
            v[i] = 1

# Iterate through the dictionary to display results
for key, value in v.items():
    # Print the vowel and its count
    print(f"Total number of '{key}' in the text is {value}")

