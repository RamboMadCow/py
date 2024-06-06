for i in range(5):
    print(i, end=" ")
else:
    print("Success!")

for i in range(5):
    print(i, end=" ")

    if i == 2:
        break
else:
    print("Success!")

i = 0

while i < 3:
    print(i, end=" ")
    i += 1

    if i == 2:
        break
else:
    print("Success!")
