'''1. Write a function in python to read the content from a text file "ABC.txt" line by line
and display the same on screen.'''


def func():
    # Prompt the user to enter content for the text file "ABC.txt"
    text = input("Enter the content for the text file \"ABC.txt\": ")

    # Open the file "ABC.txt" in write mode and write the user input into it
    with open("ABC.txt", "w") as file:
        file.write(text)

    # Open the file "ABC.txt" in read mode to read the content
    with open("ABC.txt", "r") as file:
        content = file.read()  # Read the content of the file
        print(content)  # Print the content of the file to the console


# Call the function to execute the file I/O operation
func()

'''2. Write a function in Python to count and display the total number of words in a text
file “ABC.txt”'''


def num_count():
    # Open the file "ABC.txt" in read mode to retrieve its content
    with open("ABC.txt", "r") as file:
        content = file.read()  # Read the entire content of the file

        # Split the content into words (based on spaces) and count the number of words
        print(f"Total number of words in the text file \"ABC.txt\" is: {len(content.split())}")


# Call the function to count and print the number of words
num_count()


#3. Write a function in Python to count uppercase character in a text file “ABC.txt”

def count_upper():
    # Open the file and read its content
    with open("ABC.txt", "r") as file:
        content = file.read()

        # Count uppercase letters directly and print the result
        print(f"Total number of uppercase characters in the text is: {sum(1 for i in content if i.isupper())}")


# Call the function
count_upper()

'''4. Write a function display_words() in python to read lines from a text file "story.txt",
and display those words, which are less than 4 characters.'''


def display_words():
    # Initialize an empty list to store words with less than 4 characters
    words = []

    # Take input from the user (the story)
    story = input("Write the Story: \n")

    # Write the story to the file "story.txt"
    with open("story.txt", "w") as file:
        file.write(story)

    # Open the file "story.txt" in read mode
    with open("story.txt", "r") as file:
        para = file.read()  # Read the content of the file

        # Print the full content of the story
        print(para)

        # Loop through each word in the story (split by spaces)
        for i in para.split():
            if len(i) < 4:  # Check if the length of the word is less than 4
                words.append(i)  # Add the word to the words list if it meets the condition

        # Print the list of words with less than 4 characters
        print(f"The following are the words which have less than 4 characters:\n {words}")


# Call the function to execute the word filtering
display_words()
