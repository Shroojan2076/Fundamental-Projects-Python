print('Enter \'exit\' to stop the program.')
while True:
    try:    
        num1 = input('Enter the 1st number: ')
        if num1 == 'exit':
            break
        else:
            num1 = int(num1)
        num2 = int(input('Enter the 2nd number: '))
        
        print('Which operation would you like to perform?')
        print('Addition(+)')
        print('Subtraction(-)')
        print('Multiplication(*)')
        print('Division(/)')
        ops = input('Select operation: ')
        
        if ops == '+':
            print(f'= {num1 + num2}')
        elif ops == '-':
            print(f'= {num1 - num2}')
        elif ops == '*':
            print(f'= {num1 * num2}')
        elif ops == '/':
            print(f'= {num1 / num2}')
        else:
            if num2 == 0 and ops == '/':
                print('Division by zero is not defined.')
            elif ops != '+' and ops != '-' and ops != '*' and ops != '/':
                print('Please enter valid operator.')
    except ValueError:
        print('Please enter only integer values.')
    except:
        print('Unknown error occured.')
print('Thank You!')