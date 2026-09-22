# 16. Function to find largest element in a list
def largest(num):
    max_value = num[0]

    for n in num:
        if n > max_value:
            max_value = n

    return max_value

print("Largest:", largest([10, 50, 20, 40]))
