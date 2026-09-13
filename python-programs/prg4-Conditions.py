#4) Conditions
#1. Check whether a number is positive, negative, or zero.
num = int(input("Enter a number: "))

if num > 0:
    print(num,"is Positive")
elif num < 0:
    print(num,"is Negative")
else:
    print(num,"is Zero")
print("---------------------------------")

#2. Check whether a person is eligible to vote.
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
print("---------------------------------")

#3. Find the largest of three numbers.
a = 10
b = 25
c = 15

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
print("---------------------------------")
#4. Check whether a year is a leap year.
y = int(input("Enter a year: "))

if (y % 4 == 0):
    print(y,"is Leap year")
else:
    print(y,"is Not a leap year")
print("---------------------------------")

#5. Create a grade system based on marks.
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Fail")
print("---------------------------------")

#6. Check whether a number is divisible by 5 and 11.
n = int(input("Enter a number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")
print("---------------------------------")
    
#7. Create a simple calculator using if-elif-else.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

