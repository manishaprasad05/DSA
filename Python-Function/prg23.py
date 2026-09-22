# 23. Function to sort a list without using sort()
def my_sort(num):
    result = num.copy()

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    return result

print("Sorted list:", my_sort([5, 2, 8, 1, 3]))
