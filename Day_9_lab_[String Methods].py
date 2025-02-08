'''1. Write a Python program to Count all letters, digits, and special
symbols from the given string
Input = “P@#yn26at^&i5ve”
Output: Chars = 8 Digits = 3 Symbol = 4'''

# Input string containing alphabets, numerics, and symbols
enput = "P@#yn26at^&i5ve"
print(f"Given string: \n{enput}")
# Lists to store separated characters
alphabets = []  # List to store alphabetic characters
numerics = []   # List to store numeric characters
symbols = []    # List to store special symbols

# Iterate through each character in the input string
for i in enput:
    if i.isalpha():  # Check if the character is an alphabet
        alphabets.append(i)  # Add alphabetic character to alphabets list
    elif i.isnumeric():  # Check if the character is numeric
        numerics.append(i)  # Add numeric character to numerics list
    else:  # If it's neither alphabetic nor numeric, it's a symbol
        symbols.append(i)  # Add symbol to symbols list

# Print the lists containing the separated characters
#print(alphabets)  # Print the list of alphabetic characters
#print(numerics)   # Print the list of numeric characters
#print(symbols)    # Print the list of symbols

# Print the counts of each category of characters
print(f"total number of alphabets: {len(alphabets)}")  # Count of alphabets
print(f"total number of digits: {len(numerics)}")  # Count of numeric characters
print(f"total number of symbols: {len(symbols)}")  # Count of symbols

'''2. Write a Python program to remove duplicate characters of a given
string.
Input = “String and String Function”
Output: String and Function'''

# Input string containing duplicate words
string = "String and String Function"
print(f"Input: {string}")
# Split the string into a list of words
list_of_string = string.split()  # ['String', 'and', 'String', 'Function']

# List to keep track of unique words
counter = []

# Iterate through each word in the list
for i in list_of_string:
    if i not in counter:  # Check if the word is not already in the counter list
        counter.append(i)  # Add the unique word to the counter list

# Join the unique words back into a single string and print the result
print(f"Output : {' '.join(counter)}")  # Output: "String and Function"


'''3. Write a Python program to count Uppercase, Lowercase, special
character and numeric values in a given string
Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
Output:
UpperCase : 5
LowerCase : 18
NumberCase : 5
SpecialCase : 11'''

# Input string containing uppercase, lowercase letters, numbers, and symbols
input = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
print(f"Given string: \n{input}")
# Lists to categorize characters
upper = []  # List to store uppercase letters
lower = []  # List to store lowercase letters
symbol = []  # List to store special symbols
number = []  # List to store numeric characters

# Iterate through each character in the input string
for i in input:
    if i.isupper():  # Check if the character is an uppercase letter
        upper.append(i) #Add the uppercase character in the list
    elif i.islower():  # Check if the character is a lowercase letter
        lower.append(i) #Add the lowercase character in the list
    elif i.isnumeric():  # Check if the character is a numeric digit
        number.append(i)    #Add the number character in the list
    else:  # If it's neither a letter nor a number, it's a special symbol
        symbol.append(i)    #Add the special symbol character in the list

# Print the counts of each category
print(f"UpperCase : {len(upper)}")  # Count of uppercase letters
print(f"LowerCase : {len(lower)}")  # Count of lowercase letters
print(f"NumberCase : {len(number)}")  # Count of numeric characters
print(f"SpecialCase : {len(symbol)}")  # Count of special symbols


'''4. Write a Python program to Count vowels in a string
input= “Welcome to Python Assignment”
Output: Total vowels are: 8'''

# Input text containing a sentence
text = "Welcome to Python Assignment"
print(f"In the given string: \n{text}")

# List to store the vowels found in the text
vowel = []

# Iterate through each character in the lowercase version of the input text
for i in text.lower():  # Convert text to lowercase to simplify vowel checking
    if i in ["a", "e", "i", "o", "u"]:  # Check if the character is a vowel
        vowel.append(i)  # Add the vowel to the list

# Print the total number of vowels found
print(f"Total Vowels are : {len(vowel)}")  # Output: Total Vowels are : 9
