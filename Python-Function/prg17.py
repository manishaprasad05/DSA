# 17. Function to remove duplicate elements from a list
def remove_duplicates(num):
    result = []

    for n in num:
        if n not in result:
            result.append(n)

    return result

print("Without duplicates:", remove_duplicates([10, 20, 20, 30, 30, 40]))
