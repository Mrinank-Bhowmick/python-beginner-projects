def compute():
    ans = 0
    x = 1  # Represents the current Fibonacci number being processed
    y = 2  # Represents the next Fibonacci number in the sequence
    while x <= 4000000:
        if x % 2 == 0:
            ans += x
        x, y = y, x + y
    return str(ans)


if __name__ == "__main__":
    print(compute())
