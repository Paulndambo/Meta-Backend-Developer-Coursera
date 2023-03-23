set_a = {1, 2, 3, 4, 5}
# Methods
#set_a.add(6)
#set_a.remove(5)
#set_a.discard(2)
set_b = {4, 5, 6, 7, 8}

# Union, join and remove duplicates
print(set_a.union(set_b))
print(set_a | set_b)

# Intersection, both in a and b
print(set_a.intersection(set_b))
print(set_a & set_b)

# Set Difference, only on left side not in right side
print(set_a.difference(set_b))
print(set_a - set_b)

# Symetrical Difference, all in a and b but not in both
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)