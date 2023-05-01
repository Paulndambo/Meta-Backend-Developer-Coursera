def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)

result = recursive_sum(10)
print(result)
