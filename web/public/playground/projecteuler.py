# === Project Euler · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ZackeryRSmith.

# Sum multiples of 3 or 5 below 1000
def compute():
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return str(ans)


if __name__ == "__main__":
    # Print the computed answer
    print(compute())
