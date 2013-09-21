'''
Created on 21/09/2013

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

@author: Antek
'''

def prime_numbers(n, prev = None):
    if prev == None:
        numbers = range(2, n + 1)
    else:
        numbers = prev + range(prev[-1] + 1, n)
    
    for number in numbers:
        for multiply in range(number * 2, n + 1, number):
            if multiply in numbers:
                numbers.remove(multiply)
    return numbers

def first_n_prime_numbers(n):
    current_length = n
    result = prime_numbers(current_length)
    print current_length
    while len(result) < n:
        current_length += n
        result = prime_numbers(current_length, result)
    return result[:n]
    

if __name__ == '__main__':
    
    print 'result: %s' % first_n_prime_numbers(10001)[-1]
    