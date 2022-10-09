def arithmetic_sum(number, limit):
    for last in range(limit, 1, -1):
        if last % number == 0:
            return ((limit // number) * (number + last)) // 2


def math_power():
    ans, limit = 0, 999
    ans += arithmetic_sum(3, limit)
    ans += arithmetic_sum(5, limit)
    ans -= arithmetic_sum(15, limit)
    return ans
