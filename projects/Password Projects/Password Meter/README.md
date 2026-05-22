# Password Meter

Scores the strength of a password using a set of rules. It awards points for character count, uppercase/lowercase letters, numbers and symbols, and deducts points for weaknesses such as letters-only passwords or consecutive/sequential characters.

## Example

```text
Type your password: 
Tr0ub4dor!
40 % Number of Characters
16 % Uppercase Letters
0 % Lowercase Letters
16 % Numbers
6 % Symbols
8 % Middle Numbers or Symbols
8 % Requirements
============Deductions=============
0 % Letters Only
0 % Numbers Only
-2 % Consecutive Uppercase Letters
0 % Consecutive Lowercase Letters  
0 % Consecutive Numbers
0 % Sequential Letters 
0 % Sequential Numbers
```

## How to run on localhost

```
python main.py
```

## Dependencies

Standard library only (`string`).
