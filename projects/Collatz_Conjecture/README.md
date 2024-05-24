# Collatz Conjecture Iterator

This code snippet is a simple implementation of an iterator that generates the Collatz sequence for a given positive integer greater than 1. The Collatz sequence is a process where each number transforms based on the following rules:

- If the number is even, divide it by 2.
- If the number is odd, multiply it by 3 and add 1.
- Continue this process until you reach 1.

### Overview

The provided code defines a Collatz class that initializes with a positive integer n and implements the iterator pattern to generate the Collatz sequence. The `__next__()` method computes the next number in the sequence according to the rules above. It raises a StopIteration exception when the sequence reaches 1.
#### Usage

1. When executed, the script prompts the user for a positive integer.
2. The script then iterates through the Collatz sequence, printing each number in the sequence.
3. The sequence ends when the iterator reaches 1, triggering the StopIteration exception.
4. If an invalid input is entered (like a non-integer), a ValueError is raised, prompting the user with an error message.

#### How to Run

- Run the script in your Python environment.
- In terminal write this command
 > python collatz.py


#### Error Handling

- If the input is not a valid integer, a ValueError exception is raised, prompting the user to enter a valid integer.
- If the iterator reaches 1, a StopIteration exception is raised, indicating the end of the sequence.