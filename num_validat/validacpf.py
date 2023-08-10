import re

def validates_num(num):
    num = str(num)
    num = re.sub(r'[^0-9]', '', num)

    if not num or len(num) != 11:
        return False

    new_num = num[:-2]                 # Delete the last two digits of the number
    reverse = 10                        # Reverse counter
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # First index goes from 0 to 9
            index -= 9                  # It's the first 9 digits of the number

        total += int(new_num[index]) * reverse  # Total amount of multiplication

        reverse -= 1                    # Decrement the reverse counter
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:                   # If the digit is > than 9 the value is 0
                d = 0
            total = 0                   # Reset the total
            new_num += str(d)          # Concatenate the generated digit into the new number

    # Avoid sequences. Ex.: 11111111111, 00000000000...
    sequence = new_num == str(new_num[0]) * len(num)

    # Find out which strings evaluated as true
    if num == new_num and not sequence:
        return True
    else:
        return False
