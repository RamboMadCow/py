def greet_people(age: int, *people: str):
    print(people)
    for name in people:
        print(f"Hello, {name}")
        
        
greet_people(15, "Mario", "Luigi", "Mark", "Brenda")