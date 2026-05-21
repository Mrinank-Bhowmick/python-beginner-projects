# === Collatz Conjecture Iterator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @lonelyH3b.

# Define a class to generate the Collatz sequence
class Collatz:
    # Store the starting number
    def __init__(self, n):
        self.n = n

    # Make the object usable in a for loop
    def __iter__(self):
        return self

    # Compute the next number in the sequence
    def __next__(self):
        if self.n == 1:
            # Stop when we reach 1
            raise StopIteration

        if self.n % 2 == 0:
            self.n = self.n // 2
        else:
            self.n = 3 * self.n + 1
        return self.n


if __name__ == "__main__":
    print("To generate a Collatz Sequence,")
    # Ask user for a starting number and print the sequence
    try:
        input_number = int(input("Please enter a positive integer number: "))
        for i in Collatz(input_number):
            print(i, end=" ")
    except StopIteration:
        print("Collatz sequence ended!")
    except ValueError:
        print("Input Should be an Integer!")
