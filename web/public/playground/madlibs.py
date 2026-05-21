# === Madlibs Generator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ZackeryRSmith.

# Ask the user for the five story ingredients
adjective = input("Give me an adjective: ")
animal = input("Give me an animal: ")
verb = input("Give me a verb (ending in -ing): ")
place = input("Give me a place: ")
adverb = input("Give me an adverb: ")

# Print the completed silly story
print()
print("=== Your story ===")
print()
print(f"One {adjective} morning, a {animal} was {verb} near {place}.")
print(f"It looked around {adverb} and decided today would be the day.")
print(f"And so the {animal} kept {verb} — happily ever after.")
