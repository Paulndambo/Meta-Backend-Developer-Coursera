contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
name = 'Paul'

#x = [x for x in contacts if x[0] == name][0] 
contacts_dict = {}
for x in contacts:
    contacts_dict[x[0]] = x[1]

x, y = [1, 2]
x, y = y, x


a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

a, b, c, d, *e, f, g = range(20)
print(len(e))