list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
print(*list1)

### Add Item
list1.insert(len(list1), 9)
print(list1)
list1.append(10)
list1.extend([11, 12, 13])
print(list1)

## Remove Item
list1.pop(4) # at index 4
del list1[4]

for x in list1:
    print(x)

