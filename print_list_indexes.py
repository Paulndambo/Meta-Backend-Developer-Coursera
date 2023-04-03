names = ["paul", "john", "james", "andrew", "kibe"]

for x in names:
    x_index = names.index(x)
    if x_index % 2 == 0:
        print(x, x_index)

names.reverse()
print(names)