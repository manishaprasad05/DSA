
#3) Operators
#1. Perform addition, subtraction, multiplication, and division.
a = 20
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("---------------------------------")

#2. Find the remainder and quotient of two numbers.
r = 20
q = 5
print("Remainder:", r % q)
print("Quotient:", r // q)
print("---------------------------------")

#3. Check whether a number is even or odd.
n=int(input("Enter Number:"))
if (n%2==0):
    print("Number is even")
else:
    print("Number is odd")
print("---------------------------------")

#4. Compare two numbers using relational operators.
n1=15
n2=20
print("15 == 20:", n1 == n2)
print("15 != 20:", n1 != n2)
print("15 > 20:", n1 > n2)
print("15 < 20:", n1 < n2)
print("15 >= 20:", n1 >= n2)
print("15 <= 20:", n1 <= n2)
print("---------------------------------")

#5. Demonstrate logical operators (and, or, not).
x = 10
y = 20
print("AND:", x < 20 and y > 10)
print("OR:", x > 20 or y > 10)
print("NOT:", not(x > y))
print("---------------------------------")

#6. Demonstrate assignment operators (+=, -=, *=, /=).
num = 10

num += 5
print("After +=:", a)
num -= 3
print("After -=:", a)
num *= 2
print("After *=:", a)
num /= 4
print("After /=:", a)
print("---------------------------------")

#7. Find the largest of two numbers using comparison operators.
a1 = int(input("Enter Number 1:"))
b1 = int(input("Enter Number 2:"))

if a1 > b1:
    print("Largest:", a1)
else:
    print("Largest:", b1)

