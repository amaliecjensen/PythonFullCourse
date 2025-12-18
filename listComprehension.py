items = [
    ('product1', 10),
    ('product2', 11),
    ('product3', 12),
]

# syntax = [do this for x in iterable]

items2 = [x for x in items if x[1] >= 9]
