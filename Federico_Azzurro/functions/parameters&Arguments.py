def greet(name: str, greeting: str = "Hello", age: int = 0):
    print(f"{greeting}, {name}! {age}")


greet("Bob")
greet("Mario", "Ciao")
greet("Luigi", age=18)
greet(greeting="Howdy", age=21, name="Mark")
