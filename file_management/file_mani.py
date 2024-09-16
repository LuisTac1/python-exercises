"""
Creating, reading, writing and deleting files
"""

# Creating and using file in python.
def a():
    file = open('abc.txt', 'w+')

    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')

    file.seek(0, 0)
    print('Reading lines')
    print(file.read())

    print('###############')
    file.seek(0, 0)
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.readline(), end='')

    print('###############')
    file.seek(0, 0)
    print(file.readlines())


    file.close()

    try:
        file = open('abc.txt', 'w+')
        file.write('Line')
        file.seek(0,0)
        print(file.read())
    finally:
        file.close()

# Context Manager in Python (pythonic way to work with files).
def b():
    with open('abc.txt', 'w+') as file:
        file.write('Line 1\n')
        file.write('Line 2\n')
        file.write('Line 3\n')

        file.seek(0)
        print(file.read())



# Reading files in python.
def c():
    with open('abc.txt', 'a+') as file:
        file.write('writing now... \n')
        file.seek(0)
        print(file.read())



# Creating json file.
import json

def d():
    d1 = {
        'people_1': {
            'name': 'Lui',
            'age': 20
        },
        'people_2': {
            'name': 'Rose',
            'age':30,
        }
    }

    d1_json = json.dumps(d1, indent=True)

    with open('abc.json', 'w') as file:
        file.write(d1_json)



