'''
Created on 15/09/2013

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The acc of these multiples is 23.

Find the acc of all the multiples of 3 or 5 below 1000.

http://projecteuler.net/problem=1

@author: Antek
'''

if __name__ == '__main__':
    
    acc = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            acc += x
    
    print(acc)