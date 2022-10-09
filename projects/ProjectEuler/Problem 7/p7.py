def eratosthenes():
    """Yields the sequence of prime numbers via the Sieve of Eratosthenes."""
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2  # first integer to test for primality
    while 1:
        if q not in D:
            yield q  # not marked composite, must be prime
            D[q * q] = [q]  # first multiple of q not already marked
        else:
            for p in D[q]:  # move each witness to its next multiple
                D.setdefault(p + q, []).append(p)
            del D[q]  # no longer need D[q], free memory
        q += 1


def nth_prime(n):
    for i, prime in enumerate(eratosthenes()):
        if i == n - 1:
            return prime


print(nth_prime(10001))
