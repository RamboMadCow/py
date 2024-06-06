people: list[str] = ["Mario", "Luigi", "Peach", "Toad"]

print(people)
print(len(people))
print(people[0])
print(people[0:2])
print(people[0:4])
print(people[2:4])

print("Luigi" in people)

people[0] = "Shy Guy"
print(people[0])

people[0:2] = ["Shy Guy", "Bowser"]
print(people)

people.insert(2, "!!!")
print(people)

people.append("Mario")
print(people)

people2: list[str] = ["Sonic", "Tails"]

people.extend(people2)
print(people)

new_list = people + people2
print(people)

list_2 = people
list_2 += people2
print(list_2)

people.remove("Mario")
print(people)

people.pop(2)
print(people)

people.pop()
print(people)

people.reverse()
print(people)

people.sort()
print(people)

people.clear()
print(people)
