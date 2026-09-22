# 25. Function that accepts any number of arguments using *args
def add_all(*args):
    total = 0

    for n in args:
        total += n

    return total

print("Sum using *args:", add_all(10, 20, 30, 40))
