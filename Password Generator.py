import secrets as sc
import string as s

letters = s.ascii_letters
numbers = s.digits
symbols = s.punctuation

print('Welcome to Password Generator!')

try:
    n_letters = int(input('Enter the number of letters you want in your password:\n'))
    n_numbers = int(input('Enter the number of numbers you want in your password:\n'))
    n_symbols = int(input('Enter the number of symbols you want in your password:\n'))

    if n_letters <= 0 and n_numbers <= 0 and n_symbols <= 0:
        print("Provided password length is too small.")
       
    elif n_letters >= 100 or n_numbers >= 100 or n_symbols >= 100:
        print("Provided password length is too large.")

    else:   
        password = []

        for let in range(n_letters):
            password.append(sc.choice(letters))
        for num in range(n_numbers):
            password.append(sc.choice(numbers))
        for sym in range(n_symbols):
            password.append(sc.choice(symbols))

        sysrand = sc.SystemRandom()
        sysrand.shuffle(password)
        print("Here's your new Password:")
        print("".join(password))
    
except ValueError:
    print('Please enter a valid value. Program stopped.')

