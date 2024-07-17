print("test")

# a = input("Input anythings: ")

# print(a)

# Single line comment

""" Block 
    comments
"""

greeting = "Hello "

PI = 3.1415

is_connected = False  # boolean
test = "testl"  # string
number = 100  # integer
decimal = 1.234  # float
com = 8j  # complex number

people = ["Mario,", "Luigi"]  # list
lotto_numbers = (1, 2, 3, 4, 5, 6)  # tuple
numbers = range(1, 1000)  # range

users = {'user1': 'mario123', 'user2': 'luigi123'}  # dictionary
unique_numbers = {1, 2, 2, 3, 3, 4}  # set
unique_numbers2 = frozenset({1, 2, 2, 3, 3, 4})  # frozen set

is_empty = None  # empty

name: str = "Mario"  # type hinting
integer: int = 23

print(name + str(integer))

result = name + str(integer)
print(result)

print(type(result))

number_100 = "100"
num = 10

new_results = int(number_100) + num
print(new_results)

a = 100_000_000  # _ is ignored formatting but makes numbers more read-able
