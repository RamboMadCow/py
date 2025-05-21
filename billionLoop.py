import time

startTime = time.time()
endTime = 0

for i in range(1000000000):
    pass

endTime = time.time()
print()
print(startTime)
print(endTime)
print()
print(endTime - startTime)
