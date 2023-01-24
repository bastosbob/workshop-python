#Create a generator that generate random numbers between 1 to 100.

import random

def random_number():
    while True:
        yield random.randint(1, 100)

if __name__ == '__main__':
    for i in random_number():
        print(i)
