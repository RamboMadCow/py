for i in range(10):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)

i = 0
while i < 3:
    print(i)

    if i == 1:
        break

    i += 1

print("Done!")

a, b = 10, 20

if a > b:
    # Do this thing
    pass  # Useful for stubbing things out as this if check would not run in python without this



