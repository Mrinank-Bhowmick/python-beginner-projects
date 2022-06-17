# Largest palindrome product     | https://projecteuler.net/problem=4
#-------------------------------------------------------------------------------
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#-------------------------------------------------------------------------------

#def lpp(m: int, l: int) -> int:
#    """int m: Max range for palindrome checking\nint l: length of the numbers E.g. 91 x 99 (is 2-digit)"""
#    if len(str(m)) != l: raise ValueError(f'Args "{m}"&"{l}" (m & l) do not match up.')
#    results, limit = [], range(m, int("9"*(l-1)) if not l in [1, 0] else -1 , -1)
#    [[results.append(tmp) for j in limit if str(tmp:=j*i)==str(tmp)[::-1]] for i in limit]
#    return max(results)

# One line version (split into many for readability)
lpp = lambda m : [
        results:=[],  # Store all possible results (m<)
        
        limit:=range(
            m,                                          # Start 
            int("9"*(l-1)) if not l in [1, 0] else -1,  # End
            -1                                          # Step
        ),  # Range. When used allows to maintain digit limit (definied by "l")
        
        # Calculate all possible palindromes
        [[results.append(tmp) for j in limit if str(tmp:=j*i)==str(tmp)[::-1]] for i in limit],
        
        # Get the largest palindrome product
        max(results)][3]

print(lpp(999, 3))
