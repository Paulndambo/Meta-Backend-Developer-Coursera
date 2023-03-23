import time
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

start_time = time.time()

for x in range(100):
    for j in range(1000):
        print(0, end = " ")
    print()


print(round((time.time() - start_time), 2))