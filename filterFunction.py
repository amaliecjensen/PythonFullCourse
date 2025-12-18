items = [
    ('product1', 10),
    ('product2', 11),
    ('product3', 12),
]


x = list(filter(lambda item: item[1] >= 10, items))
print(x)
