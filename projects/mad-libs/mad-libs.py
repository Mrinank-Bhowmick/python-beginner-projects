import os
import re

def madLibs(input_file, output_file):
    """lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
    Args:
        filename (str): name of file to parse
    Returns:
        None
    """
    regex = re.compile(r'(NOUN|ADJECTIVE|ADVERB|VERB)')

    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:

        content = in_file.read()

        matches = regex.findall(content)

        for found in matches:
            sub = input('Enter a ' + found + ': ')
            content = content.replace(found, sub, 1)

        out_file.write(content)
        print(content)

if __name__ == "__main__":
    madLibs('input.txt', 'output.txt')
