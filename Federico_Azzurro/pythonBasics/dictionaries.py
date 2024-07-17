users = {"user1": "Mario",
         "user2": "Luigi"}
print(users)
print(len(users))

user1 = users["user1"]
print(user1)

user2 = users.get("user2")
print(user2)

x = list(users.keys())
y = list(users.values())

print(x)
print(y)

users["user1"] = "Toad"
print(users)

a = users.items()
print(a)

users.update({"hello": 123})
print(users)

users.pop("user1")
print(users)

users.popitem()
print(users)

users.clear()
print(users)

users.update({"user1": "Mario",
              "user2": "Luigi",
              "items": {"apple": 10,
                        "banana": 20}})

print(users)
print(users["items"])
print(users["items"]["apple"])

print(users.setdefault("user1", "There is no key!"))
print(users.setdefault("xx", "There is no key!"))
