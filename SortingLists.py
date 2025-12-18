numbers = [2, 4, 5, 56, 22, 5666, 3]
numbers.sort()
numbers.sort(reverse=true)  # descending order
sorted(numbers)  # returns a new sorted list


items = [
    ('product1', 10),
    ('product2', 11),
    ('product3', 12),
]


def sort_item(item):
    return item[1]


items.sort(sort_item)  # note only passing  reference
