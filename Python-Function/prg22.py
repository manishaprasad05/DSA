# 22. Function to find second-largest number in a list
def second_largest(num):
    unique_num = list(set(num))
    unique_num.sort()

    return unique_num[-2]

print("Second largest:", second_largest([10, 50, 20, 40, 50]))
