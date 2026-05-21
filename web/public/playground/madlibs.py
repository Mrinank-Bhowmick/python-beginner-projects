# Madlibs Generator
# Fill in a few words and get back a silly story.

adjective = input("Give me an adjective: ")
animal = input("Give me an animal: ")
verb = input("Give me a verb (ending in -ing): ")
place = input("Give me a place: ")
adverb = input("Give me an adverb: ")

print()
print("=== Your story ===")
print()
print(f"One {adjective} morning, a {animal} was {verb} near {place}.")
print(f"It looked around {adverb} and decided today would be the day.")
print(f"And so the {animal} kept {verb} — happily ever after.")
