a = 0

while a < 10:
    if a > 5:
        print(True)
        print(a)
    else:
        print(False)
        print(a)
    a += 1

text = "hello"

if text == "hello":
    print("Bot: Hello!")
elif text == "bye":
    print("Bot: Goodbye!")
else:
    print("I did not understand...")

print("Success") if 1 > 2 else print("Failure")  # Python's "ternary"
b = 10
result = a if a > b else b

print(result)
