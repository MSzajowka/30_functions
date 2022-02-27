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


# 5. Snail climbing the pole - Snail climbs the X m high pole Y cm each day and slides Z cm down each night (Y must be bigger than Z). Checking in how many days the snail will reach the top of a pole.
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


# 7. Qwerty. Who decided that 'a' is the first letter of latin alphabet? Who, when and why decided that 'b' will be second and 'z' the last one? Nobody knows that. Let's assume the alphabet looks different. That it starts with 'q', then there is 'w', 'e', 'r', 't' and 'y'. The last letter in the qwerty alphabet is 'm'. This function will sort the collection in the qwerty alphabetical order.
def qwerty_sorted():
    abc_string = input("Provide string to sort: ")
    if abc_string.isnumeric():
        print('Provide a non numeric string!')
        return
    else:
        qwerty = 'qwertyuiopasdfghjklzxcvbnm'
        abc_string = abc_string.replace(' ', '').lower()
        qwerty_alphabet = {}
        i = 0
        for letter in qwerty:
            qwerty_alphabet[i] = letter
            i += 1
        sorted_string = {}
        for abc_letter in abc_string:
            for occurrence in range(0, abc_string.count(abc_letter)):
                keys = [key for key, value in qwerty_alphabet.items() if value == abc_letter]
                idx = keys[0] * (occurrence + 10000)
                sorted_string[idx] = abc_letter
        # print(sorted_string)
        # sorted_dict = sorted(sorted_string.keys())
        # final = ''
        # for sorted_letter in sorted_dict:
        #     final += sorted_letter
        # print(final)


# TODO - unfinished function!
# qwerty_sorted()

'''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
FROM THIS MOMENT I LEARNED THAT IT'S BETTER TO PROVIDE 30 SIMPLE FUNCTIONS THAN LESS BUT MORE COMPLICATED.
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
'''


# 8. Celsius to Fahrenheit or opposite
def degree_convert(degree, way):
    if way == 'cf':
        result = degree * 9 / 5 + 32

    elif way == 'fc':
        result = (5 / 9) * (degree - 32)
    else:
        result = 'Wrong conversion parameter!'
    return result


# TODO - unhasb below 4 lines
# print('Sample values - 25 C convert to F: ')
# print(degree_convert(25, 'cf'))
# print('Sample values - 70 F convert to C: ')
# print(degree_convert(77, 'fc'))


# 9. Check if X is dividable by Y.
def dividable_check(x, y):
    if x % y == 0:
        return 'dividable'
    else:
        return 'non dividable'


# TODO - unhash below line
# print(dividable_check(10, 2))


# 10. Count letters in the sentence
def count_letter(string):
    string = string.replace(' ', '')
    return len(string)


# TODO - unhash below line
# print(count_letter('To zdanie ma trzydzieści jeden liter'))


# Count words in a sentence
def count_words(string):
    string = string.split()
    return len(string)


print(count_words("To zdanie ma pięć wyrazów"))
