def reverse_string(str):
    return str[::-1]

print(reverse_string("Hello World!"))


def reverse_string_by_recursion(str):
    if len(str) == 0:
        return str
    else:
        return reverse_string_by_recursion(str[1:]) + str[0]

print(reverse_string_by_recursion("Ndambo"))