# 01. Counting the n-degree square root from x.

def square():
    x = input('Provide number which will be square rooted: ')
    n = input('Provide root: ')
    if not x.isdecimal() or not n.isdecimal():
        return ValueError
    else:
        return int(x) ** (1 / int(n))

# TODO - unhash below
# print(square())


# 02. Finding if the given number is a prime number
def find_prime_numbers():
