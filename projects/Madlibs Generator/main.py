def generate_madlib(choice, adjective, noun, verb, adverb):
    stories = {
        1: f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}.",
        2: f"In a land far away, a {adjective} {noun} decided to {verb} {adverb} every day.",
        3: f"{adjective.capitalize()} and {noun.capitalize()}, the perfect pair, went on a journey to {verb} {adverb}.",
    }

    return stories.get(choice, "Invalid choice!")


def main():
    print("Welcome to Mad Libs!")

    # Choose a Mad Lib template
    print("Choose a Mad Lib story:")
    print("1. Once upon a time")
    print("2. In a land far away")
    print("3. A perfect pair")

    choice = int(input("Enter the number of your choice (1-3): "))

    if choice not in [1, 2, 3]:
        print("Invalid choice. Please select a valid option.")
        return

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    madlib = generate_madlib(choice, adjective, noun, verb, adverb)

    print("Your Mad Lib Story:")
    print(madlib)


if __name__ == "__main__":
    main()
