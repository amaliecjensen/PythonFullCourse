point = {"x": 1, "y": 2}
print(type(point))
point = dict(x=1, y=2)


point["x"] = 10
point["z"] = 20


for key in point:
    print(key, point[key])


# dict comprehension

values = {}
for x in range(5):
    values[x] = x*2


values = {x: x*2 for x in range(5)}
print(type(values))
