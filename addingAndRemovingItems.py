letters = ['a', 'b', 'c', 'd']

# add
letters.append('k')
letters.insert(0, '-')  # adding at index

# remove
letters.pop()  # removes at the end of the list
letters.pop(0)  # removes at index
letters.remove('b')  # removes first occurence of b

del letters[0:3]  # removes a range of items

letters.clear()  # removes everything
