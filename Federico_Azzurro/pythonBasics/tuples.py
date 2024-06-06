people: tuple = ("Mario", "Mario", "Luigi", "Peach", "Shy Guy")
print(type(people))
print(people)

tuple2 = "Test1",
print(type(tuple2))

people_list: list[str] = list(people)
print(people_list)
print(type(people_list))

people_tuple: tuple = tuple(people_list)
print(people_tuple)

print(people[0])
print(people[2:4])
print(people[2:])
print(people[:2])
print("Mario" in people)

print(people.count("Mario"))
print(people.index("Peach"))

a, b, c, d, e = people
print(a)

f, *g = people
print(f)
print(*g)
