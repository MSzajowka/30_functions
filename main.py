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
        for number in range(1, number_to_check+1):
            if number_to_check % number == 0:
                i += 1
            if i > 2:
                print(f'The given number {number_to_check} IS NOT a prime number')
                return
        print(f'The given number {number_to_check} indeed is a prime number!')


# TODO - unhash below
#find_prime_numbers()
