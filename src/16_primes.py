import math

x = input("Please enter a positive integer greater than 1: ")
x = int(x)

def is_prime(num):
    if num < 2 or (num > 2 and num % 2 == 0):
        return(f'{num} is not prime.')
    elif num >= 9:
        test = 3
        max = math.floor(math.sqrt(num))
        while test <= max:
            if num % test == 0:
                return(f'{num} is not prime.')
            test += 2
        return(f'{num} is prime!')     
    else:
        return(f'{num} is prime!')

print(is_prime(x))
