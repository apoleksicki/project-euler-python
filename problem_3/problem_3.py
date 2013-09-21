'''
Created on 21/09/2013

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

@author: Antek
'''
from problem_7.problem_7 import prime_numbers


def prime_factors(n):
    factors = []
    step = 100
    length = step
    numbers = prime_numbers(length)
    
    remnant = n
    i = 0
    while remnant != 1:
        while remnant % numbers[i] != 0:
            i += 1
            if i >= len(numbers):
                length +=step
                numbers = prime_numbers(length)

        remnant = remnant / numbers[i]
        factors.append(numbers[i])
    return factors
        


if __name__ == '__main__':
    print prime_factors(600851475143)[-1]