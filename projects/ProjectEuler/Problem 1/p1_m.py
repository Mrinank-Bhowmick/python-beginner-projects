s35 = sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0)

n3 = (1000 - 1) // 3  # number of multiples of 3  (includes multiples of 15)
n5 = (1000 - 1) // 5  # number of multiples of 5  (includes multiples of 15)
n15 = (1000 - 1) // 15  # number of multiples of 15 (counted twice)

s35 = n3 * (n3 + 1) // 2 * 3 + n5 * (n5 + 1) // 2 * 5 - n15 * (n15 + 1) // 2 * 15

print(s35)
