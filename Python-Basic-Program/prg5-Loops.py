
#5) Loops
# 1. Print numbers from 1 to 10 using for loop
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

print("--------------------------------------------")
# 2. Print numbers from 10 to 1 using while loop
print("\n2. Numbers from 10 to 1:")
i = 10
while i >= 1:
    print(i)
    i -= 1

print("--------------------------------------------")
# 3. Print multiplication table of a number
print("\n3. Multiplication Table:")
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("--------------------------------------------")
# 4. Find the sum of numbers from 1 to n
print("\n4. Sum of numbers from 1 to n:")
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

print("--------------------------------------------")
# 5. Find the factorial of a number
print("\n5. Factorial:")
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial =", factorial)

print("--------------------------------------------")
# 6. Print all even numbers between 1 and 100
print("\n6. Even numbers between 1 and 100:")

for i in range(2, 101, 2):
    print(i, end=" ")

print("End--------------------------------------------")
# 7. Reverse a number using a loop
print("\n\n7. Reverse a number:")
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)

print("--------------------------------------------")
# 8. Count the digits of a number
print("\n8. Count digits:")
num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:
    while num != 0:
        num = num // 10
        count += 1

print("Number of digits =", count)

print("--------------------------------------------")
# 9. Check whether a number is prime
print("\n9. Check Prime Number:")
num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

print("--------------------------------------------")
# 10. Print Fibonacci series up to n terms
print("\n10. Fibonacci Series:")
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
