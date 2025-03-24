# Read an integer input for the number of words
N = int(input().strip())

# Initialize a list to store the words
words = []

# Loop to read N words from the input
for _ in range(0, N):
    word = input()  # Read a word
    words.append(word)  # Add the word to the list

# Loop through each word in the list
for word in words:
    A1 = ''  # Initialize a string to store characters at even indices
    A2 = ''  # Initialize a string to store characters at odd indices

    # Loop through each character in the word
    for i in range(0, len(word)):
        if i % 2 == 0:  # Check if the index is even
            A1 += word[i]  # Add the character to A1
        else:  # If the index is odd
            A2 += word[i]  # Add the character to A2

    # Print the characters at even indices and odd indices separated by a space
    print('{} {}'.format(A1, A2))