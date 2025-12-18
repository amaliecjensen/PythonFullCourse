items = [
    ('product1', 10),
    ('product2', 11),
    ('product3', 12),
]


items.sort(key=lambda item: item[1])  # note only passing  reference


prices = []

for item in items:  # returns list of prices
    prices.append(item[1])


map(lambda item: items[1], items)  # returns a map of prices
