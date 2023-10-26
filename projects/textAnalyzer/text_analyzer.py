"""
The proper way to utilize Python's built in efficiencies:
def count_char(text, char):
    return text.count(char)
print(count_char(text, "r"))"""
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

print(count_char(text,'a'))

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))
