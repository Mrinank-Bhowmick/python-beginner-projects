# Sum Square Difference

The sum of the squares of the first ten natural numbers is:
$1^2 + 2^2 + ... + 10^2 = 385$

The square of the sum of the first ten natural numbers is:
$(1+2 + ....+ 10)^2 = 55^2 = 3025$

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$

Find the difference between the sum of the sqaures of the first one hundred natural numbers and the square of the sum.


-----
## Brute Force Method

```python
limit = 100
sum_sq = 0
sum = 0   
for i = 1 to limit do
    sum = sum + i
    sum_sq = sum_sq + $i^2$
end for
print( $sum^(2)$ - sum_sq)
```




But this is a Brute force method. The

## Efficient Method




We know 
Sum of $n$ natural numbers:
$S = n(n+1)/2$

We are looking for a function $f(n)$ that for any $n$ gives the sum of $1^2$ up to $n^2$. Assume it is of the form $f(n) = an^3 + bn^2 + cn + d$, where $a,b,c,d$ are constants that we need to determine.  This we can get by $f(0) = 0$, $f(1) = 1$, $f(2) = 5$ , $f(3) = 14$. This gives us:

$d = 0$

$a + b + c +d = 1$

$8a + 4b + 2c + d = 5$

$27a + 9b + 3c + d = 14$

Solving this we get:
$f(n) = \frac{1}{6}(2n^3 + 3n^2 + n)  = \frac{n}{6} (2n+1) (n+1)$

hence :
```python
limit = 100
sum = limit(limit + 1)/2
sum_sq = (2limit + 1)(limit + 1)limit/6
print sum*sum - sum_sq
```




----

Answer : 25164150
