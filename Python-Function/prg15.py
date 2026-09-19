# 15. Function to find sum of all elements in a list
def sum_all(numbers):
    total = 0

    for n in numbers:
        total += n

    return total

print("List sum:", sum_all([10, 20, 30, 40]))
