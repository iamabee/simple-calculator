# Simple calculator
def welcome():
    print('''Welcome to Calculator''')
welcome()
def calculate():
    num1 = int(input("Enter first value:"))
    num2 = int(input("Enter second value:"))
    operator = input('''
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for modulus
    ''')

    if operator == '+':
        print('{} + {} ='.format(num1, num2))
        print(num1 + num2)

    elif operator == '-':
        print('{} - {} ='.format(num1, num2))
        print(num1 - num2)

    elif operator == '*':
        print('{} * {} ='.format(num1, num2))
        print(num1 * num2)

    elif operator == '/':
        print('{} / {} ='.format(num1, num2))
        print(num1 / num2)

    elif operator == '**':
        print('{} ** {} ='.format(num1, num2))
        print(num1 ** num2)

    elif operator == '%':
        print('{} & {} ='.format(num1, num2))
        print(num1 % num2)
    else:
        print("Please perform the task!")

    # Define function Again() to ask user if they want to run the program again
def again():
    # Takes input from user
    calc_again = input(''' Do you want to use calculator again?
    type Y if Yes and N for No ''')

    # If user inputs Y, the program runs again
    if calc_again.upper() == 'Y':
        calculate()

    # If user inputs N, the program terminates
    elif calc_again.upper() == 'N':
        print("See you Later.")

    # If user inputs any key, the program ask to input again
    else:
         again()
calculate()