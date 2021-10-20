# Program to check if a number is prime or not

from math import sqrt

def check_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

print(check_prime(int(input("Input a Number"))))