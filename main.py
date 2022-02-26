from random import randint, shuffle


# 01. Counting the n-degree square root from x.

def square():
    x = input('Provide number which will be square rooted: ')
    n = input('Provide root: ')
    if not x.isdecimal() or not n.isdecimal():
        raise ValueError('Value you gave is not a number dude!')
    else:
        return int(x) ** (1 / int(n))


# TODO - unhash below
# print(square())


# 02. Finding if the given number is a prime number
def find_prime_numbers():
    number_to_check = input("Provide the number to check if it's a prime number: ")
    if not number_to_check.isnumeric():
        raise ValueError('Value you gave is not a number dude!')
    else:
        number_to_check = int(number_to_check)
        i = 0
        for number in range(1, number_to_check + 1):
            if number_to_check % number == 0:
                i += 1
            if i > 2:
                print(f'The given number {number_to_check} IS NOT a prime number')
                return
        print(f'The given number {number_to_check} indeed is a prime number!')


# TODO - unhash below
# find_prime_numbers()


# 3. Rock, paper and the scissors(you, oponent).
# from random import randint

you = 0
oponent = 0


def scissors(you, oponent):
    print(f'The current result is: YOU={you}, COMPUTER={oponent}')
    user = input("\n\nChoose: (R)ock, (P)aper or the (S)cissors: ")
    print('\n')
    if user.lower() != 'r' and user.lower() != 'p' and user.lower() != 's':
        print('You did not choose (R)ock, (P)aper or the (S)cissors! Try again.')
        scissors(you, oponent)
        return (you, oponent)
    else:
        computer = randint(1, 3)
        if computer == 1:
            computer = 'r'
            print('Computer chose ROCK.')
        elif computer == 2:
            computer = 'p'
            print('Computer chose PAPER.')
        else:
            computer = 's'
            print('Computer chose SCISSORS.')
        if user == computer:
            print('Draw! You both chose the same.')
            scissors(you, oponent)
            return (you, oponent)
        if user == 'r' and computer == 'p':
            print('You lose!')
            oponent += 1
            scissors(you, oponent)
            return (you, oponent)
        elif user == 'r' and computer == 's':
            print('You WIN!')
            you += 1
            scissors(you, oponent)
            return (you, oponent)
        if user == 'p' and computer == 's':
            print('You lose!')
            oponent += 1
            scissors(you, oponent)
            return (you, oponent)
        elif user == 'p' and computer == 'r':
            print('You WIN!')
            you += 1
            scissors(you, oponent)
            return (you, oponent)
        if user == 's' and computer == 'r':
            print('You lose!')
            oponent += 1
            scissors(you, oponent)
            return (you, oponent)
        else:
            print('You WIN!')
            you += 1
            scissors(you, oponent)
            return (you, oponent)


# TODO - unhash below line
# scissors(you, oponent)


## 4. Check if word is a palindrome (read from start to end and oposite is the same).
def check_palindrome():
    string = input("Provide word to check: ")
    if string.isnumeric():
        print('You have not provide a word, but numeric value! ')
        return
    else:
        string = list(string)
        if string == string[::-1]:
            string = ''.join(string)
            print(f"Word {string} is a palindrome.")
        else:
            string = ''.join(string)
            print(f"Word {string} is NOT a palindrome.")


# TODO - unhash below line
# check_palindrome()


# 5. Snail climbing the pole - Snail claims the X m high pole Y cm each day and slides Z cm down each night (Y must be bigger than Z). Checking in how many days the snail will reach the top of a pole.
def check_snail():
    pole = input("Provide the pole's height in meters: ")
    up = input("Provide how many centimeters does the snail climb up each day: ")
    down = input("Provide how many centimeters does the snail slide down each night (must be less then way up): ")

    if not pole.isnumeric() or not up.isnumeric() or not down.isnumeric():
        print('Some value is not numeric!')
        return
    else:
        pole = float(pole)
        pole = pole * 100
        pole = int(pole)
        up = int(up)
        down = int(down)
        if up <= down:
            print("We're assuming the snail clims faster than slides down!")
            return
        else:
            if pole <= up:
                print("Snail will reach pole's top in (less than) one day :P")
                return
            else:
                print(f"The snail will reach pole's top in {(pole - down - 1) // (up - down) + 1} day(s)")


# TODO - unhash below line
# check_snail()

# from random import shuffle


# 6. Shuffle words in a sentence to receive a new funny sentence.
def shuffle_words():
    sentence = input("Provide sentence to shuffle words: ")
    if sentence.isnumeric() or not (' ' in sentence):
        print('Provide a non numeric string with words in it!')
    else:
        words = sentence.lower().split()
        # old_words = words
        # while words == old_words:
        #     shuffle(words)
        shuffle(words)
        new_sentence = ' '.join(words)

        print(f'{new_sentence.capitalize()}.')

# TODO - unhash below line
# shuffle_words()
