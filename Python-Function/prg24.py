# 24. Function to merge two lists and remove duplicates
def merge_lists(list1, list2):
    result = []

    for n in list1 + list2:
        if n not in result:
            result.append(n)

    return result

print("Merged list:", merge_lists([1, 2, 3], [3, 4, 5]))
