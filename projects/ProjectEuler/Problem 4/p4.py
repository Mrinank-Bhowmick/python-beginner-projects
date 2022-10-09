print(
    max(
        a * b
        for a in range(100, 1000)
        for b in range(a, 1000)
        if str(a * b) == str(a * b)[::-1]
    )
)
