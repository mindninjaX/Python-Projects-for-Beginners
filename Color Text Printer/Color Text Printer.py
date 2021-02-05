import colorama
# Back for background, Fore for text color
from colorama import Back, Fore

# This line is make sure that the color style resets once the execution of program is complete
colorama.init(autoreset = True)

text = input("Enter a pharse or sentence: ")

# Colorama has limited color options
print(Fore.BLACK + Back.WHITE  + text)
print(Fore.RED + Back.CYAN  + text)
print(Fore.GREEN + Back.MAGENTA  + text)
print(Fore.YELLOW + Back.BLUE  + text)
print(Fore.BLUE + Back.YELLOW  + text)
print(Fore.MAGENTA + Back.GREEN  + text)
print(Fore.CYAN + Back.RED  + text)
print(Fore.WHITE + Back.BLACK  + text)
