"""
Simple Calculator
"""

n1 = 0
n2 = 0
result = 0
operator = ''

while True:
    n1 = int(input('Enter number 1: '))

    operator = input('Enter the operation: ')

    n2 = int(input('Enter number 2: '))

    if operator == '+':
        result = n1 + n2

    elif operator == '-':
        result = n1 - n2

    elif operator == '*':
        result = n1 * n2

    elif operator == '/':
        result = n1 / n2

    else:
        print('Invalid operation')


    print(f'{n1} {operator} {n2} = {result}')


