# Taking user input 
user_input = input("Enter a phrase: ")

# Getting rid of 'of' word using replace() method & Spiliting the user input into individual words using split() method
phrase = (user_input.replace('of', '')).split()

# Initializing an empty string to append the acronym
a = ""

# for loop to append acronym
for word in phrase:
    a = a + word[0].upper()

print(f'Acronym of {user_input} is {a}')