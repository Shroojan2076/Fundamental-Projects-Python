import random as rd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print('Welcome to Password Generator!')

try:
    n_letters = int(input('Enter the number of letters you want in your password:\n'))
    n_numbers = int(input('Enter the number of numbers you want in your password:\n'))
    n_symbols = int(input('Enter the number of symbols you want in your password:\n'))

    password = ''
    for s in range(n_letters):
        password += rd.choice(letters)
    for s in range(n_numbers):
        password += rd.choice(numbers)
    for s in range(n_symbols):
        password += rd.choice(symbols)
    l = list(password)
    rd.shuffle(l)
    password = "".join(l)
    print("Here's your new Password:")
    print(password)

except ValueError:
    print('Please enter a valid value. Program stopped.')