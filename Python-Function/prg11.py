# 11. Function to find maximum of three numbers

def max_three(a, b, c):
    if a >= b and a >= c:
        print("A is Maximum")
    elif b >= a and b >= c:
        print("B is Maximum")
    else:
        print("C is Maximum")
max_three(10, 55, 15)
