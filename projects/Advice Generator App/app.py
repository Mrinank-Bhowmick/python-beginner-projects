import random

# Predefined list of advice
advice_list = [
    "Stay positive and keep smiling.",
    "Don't sweat the small stuff.",
    "Take a break when you need it.",
    "Set achievable goals.",
    "Learn from your mistakes.",
    "Listen more, speak less.",
    "Practice gratitude daily.",
]

def generate_advice():
    # Generate random advice from the list
    return random.choice(advice_list)

def main():
    print("Welcome to the Advice Generator App!")
    
    while True:
        user_input = input("Press Enter to get advice, or 'q' to quit: ").strip()
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        else:
            advice = generate_advice()
            print("Here's your advice: ")
            print(advice)

if __name__ == "__main__":
    main()
