from random import randint


def generat_num():
    number = str(randint(100000000, 999999999))

    new_num = number  # 9 random numbers
    reverse = 10  # Reverse counter
    total = 0  # The total of the multiplications

    # Loop of the number
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(new_num[index]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            new_num += str(d)

    return new_num
