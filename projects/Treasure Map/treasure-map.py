line1 = ["⬜️","️⬜️","️⬜️"] #x-coordinates are A, B, and C. While y-coordinates are 1, 2 and 3.
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ") 

letter = position[0].upper()
coordinate_x = ["A", "B", "C"]
number_index = int(position[1]) - 1
letter_index = coordinate_x.index(letter)
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")