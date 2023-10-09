def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

def main():
    print("Palindrome Checker App")

    while True:
        user_input = input("Enter a word or phrase (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        result = is_palindrome(user_input)

        if result:
            print(f'"{user_input}" is a palindrome!\n')
        else:
            print(f'"{user_input}" is not a palindrome.\n')

if __name__ == "__main__":
    main()
