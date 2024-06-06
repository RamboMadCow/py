items: set = {"apple", "banana", 10, True, True, 10}  # no duplicates are kept
print(items)  # order is not set or maintained
print(len(items))

items_2: list[str] = ["One", "Two", "Three"]
items_set: set = set(items_2)
print(items_set)

items.add("orange")
print(items)

people = set()  # empty set

items.update(["carrot", 15])
print(items)

items.remove("apple")
print(items)

items.discard(10)
print(items)

items2: set = {"peper", 20, "apple", "banana"}

new_set = items.union(items2)
print(new_set)

newer_set: set = items | items2
print(newer_set)

items |= items2
print(items)

items.intersection_update(items2)
print(items)

items.symmetric_difference_update(items2)
print(items)
