def is_divisible_to(number, x):
    for i in reversed(list(range(1, x + 1))):
        if number % i != 0:
            return False
    return True


def divisible_to(x):
    if x < 1:
        return False
    elif x == 1:
        return 1
    else:
        step = divisible_to(x - 1)
        number = 0
        found = False
        while not found:
            number += step
            found = is_divisible_to(number, x)
        return number


print(divisible_to(20))
