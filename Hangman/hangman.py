"Hangman Game"
import random

word = ["table", "hammer", "car"]
secret_word = random.choice(word)
discovered_letters = []

print("="*55)
print("*"*20, "Hangman", "*"*20)
print("="*55)

for i in range(0, len(secret_word)):
    discovered_letters.append("-")

win = False

while win == False:
    letter = str(input("Type the letter: "))

    for i in range(0, len(secret_word)):
        if letter == secret_word[i]:
            discovered_letters[i] = letter

        print(discovered_letters[i])

    win = True


    for x in range(0, len(discovered_letters)):
        if discovered_letters[x] == "-":
            win = False

