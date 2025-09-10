import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
allchar = upper + lower + num + string.punctuation

n = int(input('\nEnter length of your password: '))

def simple(n):
    return ''.join(random.choice(upper + lower + num) for _ in range(n))

def hard(n):
    return ''.join(random.choice(allchar) for _ in range(n))

def choice(n):
    while True:
        z = input('Press 1 for simple password\nPress 2 for complex password\n> ')
        if z == '1':
            return simple(n)
        elif z == '2':
            return hard(n)
        else:
            print(' Wrong input, please enter 1 or 2.')


password = choice(n)
print("\n Your Generated Password is:", password)
