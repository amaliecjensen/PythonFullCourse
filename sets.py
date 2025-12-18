numbers = [1, 1, 2, 3, 4]
first = set(numbers)

print(first)  # 1 is not repeated


second = {1, 5}

second.add(5)
second.remove(5)
len(second)

print(type(second))


first | second  # all the numbers combined no dupli
first & second  # the numbers that exists in both
first - second
first ^ second

first[0]  # U CANT DO THIS SETS ARE UNORDERED COLLECTION OF UNIQUE ITEMS
