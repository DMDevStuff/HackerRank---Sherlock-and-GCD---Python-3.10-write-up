##    https://www.hackerrank.com/challenges/sherlock-and-gcd/problem
##
##    Sherlock is stuck while solving a problem: Given an array of integers A,
##    he wants to know if there exists a subset B of this array which follows
##    these statements:
##
##        B is a non-empty subset
##        There exists no integer greater than one that divides all elements of B
##        There are no elements of B which are equal to one another

##### ##### ##### #####

#   O(n * (log m))
#   n is the number of elements in the given array
#   log m is the time complexity of finding the GCD
#   at each step, where m is the min(a, b)

#   Idea:
#       GCD is a commutative property
#       For example:
#           GCD([a,b,c]) =
#           GCD(GCD([a,b]),[c])
#       With this in mind we simply find the GCD of the first two elements
#       of array A - call this g, then we find the GCD of the next element and g.
#       If at any point the current GCD equals 1, return yes
#       If we make it all the way through the given array, return no
#   Edge Case:
#       If the given array contains only one number we check for primality
#       If prime return yes, else no

#   Algo:
#       1. Check for the edge case of a single element array, if it exists,
#           check for primality(seperate function), if prime - return yes
#           else return 'no' => primality testing is expensive but because
#           this is an edge case and predictably rare, we can say the cost
#           is amortized.

#       If there is no edge case we continue.

#       2. Initalize a variable to store the current GCD at each step => O(1)
#       2. Find and store the GCD of the first two elements of the array => O(log m)
#       3. If the GCD is 1 return 'yes' => O(1)
#       4. For each successive element in the array, find the GCD of that element and
#           current GCD.  If current GCD = 1 return 'yes' if the end of the array
#           is reached return 'no' => O(n * (log m))

##### ##### ##### #####

import math

##### ##### ##### #####

#   'smart' brute force
#   for any given array it is guarenteed this function
#   will only be called once

def isPrime(a):

    if a == 2:
        return True
    if a < 2 or a % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(a))+1, 2):

        if a % i == 0:
            
            return False

    return True

##### ##### ##### #####

#   recursive implementation of euclid's algorithm
#   O(log min(a, b))

def GCD(a, b):

    if a == 0:
        return b
    if b == 0:
        return a
    
    return GCD(b, (a%b))

##### ##### ##### #####

#   main

def solve(array):

    #####

    # find and handles edge cases

    if len(array) == 1:

        if isPrime(array[0]):

            return 'YES'

        return 'NO'

    #####
    
    a = max(array[0], array[1])
    b = min(array[0], array[1])
    
    current_gcd = GCD(a, b)
    
    if current_gcd == 1:
        
        return 'YES'
    
    for index in range(2, len(array)):
        
        a = max(array[index], current_gcd)
        b = min(array[index], current_gcd)
        
        current_gcd = GCD(a, b)
        
        if current_gcd == 1:
            
            return 'YES'
        
    return 'NO'
