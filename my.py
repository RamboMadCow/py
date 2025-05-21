grade = 72

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


# Python's Ternary
ask_price = 100

if ask_price > 50:
    volume = 50
else:
    volume = 80

print(volume)


volume = 50 if ask_price > 50 else 80

print(volume)


a = 10
b = 20

distance = a - b if a >= b else b - a
print(distance)

# Lists defined by []
a = [10, 20, 30, 40, 50]
print(a[2])
print(len(a))

b = []
b.append(10)
b.append(20)
b.append(30)
b.append(40)
b.append(50)
# print(b)

b[2] = True
print(b)

print(type(b))

print(a[-1])

new_list = list()
print(new_list, type(new_list))

# Tuples defined by ()
t = (10, 20, 30)
t2 = 10, 20, 30

len(t)
print(t[0])

# t[1] = 2  // Invalid as Tuples are immutable

tupleOfList = ([1, 2], [3, 4])
print(tupleOfList[0], type(tupleOfList[0]))

# tupleOfList[0] = 100 // Invalid for same reason as above
l1 = tupleOfList[0]
l1[0] = 100
print(tupleOfList)

tupleOfList[1][1] = 400
print(tupleOfList)

implicitTuple = 1, 2
print(type(implicitTuple))

myL = [1, 2, 3]
t = tuple(myL)
print(t)

t = (10, 20, 30)
myL = list(t)
print(myL)

t = 10, 20, 3, 40
print(t)
myL = list(t)
myL[2] = 30
t = tuple(myL)
print(t)

# object reference example - Pay attention to which object is modified
t = [1, 2], 30, 40
print(t)
myL = list(t)
myL[0][0] = 10
print(t)

# Strings - Container type, Sequence, homogeneous, immutable
s = "Python rocks!"
print(s[0])
print(s[len(s) - 1])
print(len(s))
print(s[-1])
print(s[-2])

myL = list("abcdef")
print(myL)

s = "===================="  # tedious
print(s)

s = "=" * 20  # Can be used for all sequences
print(s)

myL = [0] * 10
print(myL)

#  Object reference is persistent even when using quick multiplication
myT = ([1, 2], 30)
myT2 = myT * 3
print(myT2)

print(myT2[0] is myT[0])

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print(m[0][0], m[0][1], m[2][2])
row_1 = m[0]
print(row_1)
row_1[0] = 1
print(m)
m[1][1] = 1
m[2][2] = 1
print(m)

# Slicing Sequences
s = "Python rocks!"
print(s[5])
print(s[0:5])
print(s[0:5 + 1])

t = (1, 2, 3, 4, 5)
print(t[1:4])

l1 = [1, 2, 3, 4, 5]
l2 = l1[0:3]
print(l2)

print(l1 is l2)
l2[0] = 100

print(l2, l1)
l3 = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
print(l3)

sub = l3[0:2]
print(sub)
sub[1] = "Python"
print(sub)
print(l3)

print(sub[0] is l3[0])
sub[0][0] = 100
print(sub)
print(l3)

s = "Python rocks!"
print(s[7:])
print(s[:6])

nl = [1, 2, 3, 4, 5]
nl2 = nl[:]  # This is a shallow copy, not same object
print(nl2)
print(nl is nl2)
print(nl[0] is nl2[0])
nl[0] = 100
print(nl2)

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(s[1:8])
print(s[1:8:2])
print(s[1::2])
print(s[0::2])
print(s[::2])

s = "abcdef"
print(s[-4])
print(s[-1])
print(s[-4:-1])
print(s[-1:-4])  # step is positive while final value is going backwards
print(s[-1:-4:-1])
print(s[:-4:-1])
print(s[2::-1])
print(s[::-1])

a = "racecar"
print(a == a[::-1])
a = "hello"
print(a == a[::-1])
