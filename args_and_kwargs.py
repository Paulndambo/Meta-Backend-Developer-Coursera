def sum_of_args(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


print(sum_of_args(45, 89, 9, 9, 7))


def sum_of_kwargs(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_of_kwargs(coffee=4.56, tea=5.60, mandazi=34))