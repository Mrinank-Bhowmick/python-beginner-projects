# without any clever math


def compute():
    '''Computes the sum of the multiples af 3 and 5 between 0 and 1000'''
    
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return str(ans)


if __name__ == "__main__":
    print(compute())
