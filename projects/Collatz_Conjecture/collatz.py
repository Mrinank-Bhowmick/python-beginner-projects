class Collatz:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 1:
            raise StopIteration
        if self.n % 2 == 0:
            self.n = self.n // 2
        else:
            self.n = 3 * self.n + 1
        return self.n
    


if __name__ == '__main__':
    print("To generate a Collatz Sequence, please provide an integer positive number")
    try:
        input_number = int(input("Please enter a number: "))
        for i in Collatz(input_number):
            print(i, end=" ")
    except StopIteration:
        print("Collatz sequence ended!")
    except ValueError:
        print("Input Should be an Integer!")