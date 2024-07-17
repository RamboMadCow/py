print(1 - 2)
print(2 * 2)
print(10 / 3)
print(2 / 5)
print(10 % 3)
print(10 ** 3)
print(10 // 3)

a = 5
b = 10

a += 3
print(a)

print(10 == 5)
print(10 == 5 + 5)
print(10 != 5)
print(10 < 5)
print(10 > 5)
print(10 <= 10)
print(10 >= 10)

a = 5

print(a < b and 4 < 6)
print(a < b and 4 > 6)
print(a < b or 4 > 6)

a = 100.0
b = 1.0 * a

print(id(a))
print(id(b))
print(a is b)  # dangerous
print(a == b)

numbers_1 = [1, 2, 3, 4, 5]
print(4 in numbers_1)
print(10 in numbers_1)
