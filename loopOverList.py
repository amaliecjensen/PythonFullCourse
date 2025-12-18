letters = ['a', 'b', 'c', 'd']

for letter in letters:
    print(letter)


for letter in enumerate(letters):  # returns a tuple
    print(letter[0], letter[1])
