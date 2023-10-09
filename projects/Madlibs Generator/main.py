import tkinter as tk


def generate_madlib(choice, adjective, noun, verb, adverb):
    stories = {
        1: f"""In a mystical and distant land, there was a brave and {adjective} explorer named {noun}. {noun.capitalize()} had always dreamed of {verb} {adverb} to discover hidden treasures. One day, while {verb} {adverb} deep in the dense {adjective} jungle, {noun} stumbled upon an ancient {noun}.
        The {noun} was covered in {adjective} vines and moss, but it {verb} {adverb} with the promise of untold riches. With {adjective} excitement, {noun} began to {verb} {adverb}, clearing away the obstacles that blocked the path to the treasure.
        As {noun} finally reached the heart of the {noun}, a {adjective} light {verb} {adverb}, revealing the most incredible sight. It was a chest filled with {adjective} {noun}, {adjective} jewels, and {adjective} artifacts beyond imagination. {noun} couldn't believe {noun}'s {adjective} luck!
        With the treasure in {noun}'s possession, {noun} decided to {verb} {adverb} back home and share the {adjective} riches with {noun}'s {adjective} village. And so, {noun} became a {adjective} hero and lived {adverb} ever after.
        """,
        2: f""" In the enchanting world of {noun}, there existed a {adjective} school known as the {adjective} Academy of {noun}. This {adjective} institution was no ordinary school; it specialized in teaching {adjective} magic to {adjective} students from all walks of life.
        Our {adjective} protagonist, {noun}, had always dreamed of {verb} {adverb} and becoming a {adjective} wizard. One day, {noun} received a letter of acceptance to the {adjective} Academy of {noun}. {noun} couldn't believe {noun}'s {adjective} luck!
        At the academy, {noun} learned to {verb} {adverb}, brew {adjective} potions, and cast {adjective} spells. {noun}'s favorite class was {adjective} magical creatures, where {noun} befriended a {adjective} {noun} named {noun}. Together, they embarked on a {adjective} journey to {verb} {adverb} and uncover the secrets of the {adjective} forest.
        As the years passed, {noun} became a {adjective} wizard, known for {verb} {adverb} and {verb} {adverb}. The {adjective} adventures at the academy shaped {noun}'s destiny, and {noun} went on to {verb} {adverb} and make the world a {adjective} place with {noun}'s {adjective} magic.
        """,
        3: f"""In the bustling city of {noun}, there lived a brilliant {adjective} scientist named Dr. {noun}. Dr. {noun} was renowned for {verb} {adverb} and pushing the boundaries of {adjective} science. One day, Dr. {noun} had a {adjective} idea that would change the course of history.
        With a {adjective} gleam in {noun}'s eye, {noun} decided to build a {adjective} time machine. This incredible invention would allow {noun} to {verb} {adverb} to any point in history. It was an {adjective} and {adjective} endeavor, but Dr. {noun} was determined to make it work.
        After countless {adjective} experiments and {adjective} calculations, the time machine was finally ready. Dr. {noun} stepped inside the {noun}, set the {noun} to a random date, and {verb} {adverb} into the unknown.
        As Dr. {noun} arrived in a {adjective} era, {noun} was greeted by {adjective} sights and {adjective} sounds. {noun} couldn't believe {noun}'s {adjective} eyes! {noun} encountered {adjective} figures from the past, witnessed {adjective} events, and even had the chance to {verb} {adverb} with historical legends.
        But as the {noun} continued, Dr. {noun} realized that messing with time could have {adjective} consequences. The fabric of history was fragile, and any {adjective} change could alter the course of {noun}'s own existence.
        With a {adjective} heart, Dr. {noun} returned to the present, vowing to use {noun}'s {adjective} knowledge responsibly. The time-traveling experiment was an {adjective} adventure that taught {noun} the value of {verb} {adverb} with the past while preserving the {adjective} future.
        """,
    }

    return stories.get(choice, "Invalid choice!")


def generate_madlib_button_click():
    choice = int(choice_var.get())
    adjective = adjective_entry.get()
    noun = noun_entry.get()
    verb = verb_entry.get()
    adverb = adverb_entry.get()

    madlib = generate_madlib(choice, adjective, noun, verb, adverb)

    madlib_text.config(text="Your Mad Lib Story:\n" + madlib)


# Create the main window
root = tk.Tk()
root.title("Mad Libs Game")

#
choice_label = tk.Label(
    root,
    text="""
Choose a Mad Lib story : 
1.In a mystical and distant land..  
2.In the enchanting world of...  
3.In the bustling city of...""",
)

choice_label.pack()
choice_var = tk.StringVar()
choice_var.set("1")
choice_entry = tk.Entry(root, textvariable=choice_var)
choice_entry.pack()

# USER INPUTS
noun_label = tk.Label(root, text="Enter a noun:")
noun_label.pack()
noun_entry = tk.Entry(root)
noun_entry.pack()

adjective_label = tk.Label(root, text="Enter an adjective:")
adjective_label.pack()
adjective_entry = tk.Entry(root)
adjective_entry.pack()

verb_label = tk.Label(root, text="Enter a verb:")
verb_label.pack()
verb_entry = tk.Entry(root)
verb_entry.pack()

adverb_label = tk.Label(root, text="Enter an adverb:")
adverb_label.pack()
adverb_entry = tk.Entry(root)
adverb_entry.pack()

# GENERATE MAD LIB BUTTON
generate_button = tk.Button(
    root, text="Generate Mad Lib", command=generate_madlib_button_click
)
generate_button.pack()

# MAD LIB TEXT
madlib_text = tk.Label(root, text="")
madlib_text.pack()

# Start the main event loop
root.mainloop()
