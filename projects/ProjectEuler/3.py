# Largest prime factor     | https://projecteuler.net/problem=3
#-------------------------------------------------------------------------------
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#-------------------------------------------------------------------------------
def primes(n: float, tmp=[]) -> list:    
    for i in range(3,int(__import__("math").sqrt(n))+1,2): 
        while n % i== 0: (tmp.append(i), n := n/i)
    if n > 2: tmp.append(n)
    return tmp
         
print(max(primes(600851475143)))
