a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 interger division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division

print()
# for i in range(1, a / b): Causes an exception because loops must have integers
#     print(i)

print()
for i in range(1, a // b):
    print(i)