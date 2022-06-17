# Smallest multiple     | https://projecteuler.net/problem=5
#-------------------------------------------------------------------------------
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?
#-------------------------------------------------------------------------------
def sm(to: int) -> int:
    """int to: 1-?"""
    divisors = [x for x in range(1,(to+1))]
    for i in range(2520,__import__("sys").maxsize,to):
        if(all(i%x == 0 for x in divisors)): return i

print(sm(20))
