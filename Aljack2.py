import operator
items = [
    ("ITEM 1", 1.25),
    ("ITEM 2", 0.75),
    ("ITEM 3", 1.0),
    ("ITEM 4", 2.5),
    ("ITEM 5", 3.0)
]

sorted_items = sorted(items, key=operator.itemgetter(1), reverse=True)

for item in sorted_items:
    print(item)
