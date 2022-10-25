# this is an attempt to create a story with the user's input.
from errno import WSAETOOMANYREFS


name=input("What is the name of the main character in your story?") 
gender=input("What is your character's gender? man or woman?")
age=input("How old is he or she? ")
nationality=input("What nationality is your character?")
place=input("Where does this story take place?")

print(f'There was a {gender} called {name}. {name} was a {age} years old {nationality}.I met {name} in {place} during my short visit there. Our encounter was nothing short of interesting. One it seems I may never forget.')