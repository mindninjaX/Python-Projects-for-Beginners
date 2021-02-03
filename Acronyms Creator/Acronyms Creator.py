# Taking user input 
user_input = input("Enter a phrase: ")

# Spiliting the user input into individual words using split() method
phrase = user_input.split()

# Initializing an empty string to append the acronym
a = ""

# for loop to append acronym
for word in phrase:
    a = a + word[0].upper()

print(a)