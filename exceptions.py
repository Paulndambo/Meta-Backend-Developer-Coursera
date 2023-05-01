def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 'f')
except ZeroDivisionError as e:
    print("Something Wrong Happened!", e)
except Exception as e:
    print("Something Wrong Happened!", e)
