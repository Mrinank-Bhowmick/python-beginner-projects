# Defined a class to generate Collatz Sequence
class Collatz:
    # Constructor to initialize the number
    def __init__(self, n):
        self.n = n

    # Iteration method
    def __iter__(self):
        return self

    # Next method to generate next number in the sequence
    def __next__(self):
        if self.n == 1:
            # Stop iteration when the number is 1
            raise StopIteration

        if self.n % 2 == 0:
            self.n = self.n // 2
        else:
            self.n = 3 * self.n + 1
        return self.n


# Main function to test the class
if __name__ == "__main__":
    print("To generate a Collatz Sequence,")
    try:
        input_number = int(input("Please enter a positive integer number: "))
        for i in Collatz(input_number):
            print(i, end=" ")
    except StopIteration:
        print("Collatz sequence ended!")
    except ValueError:
        print("Input Should be an Integer!")
