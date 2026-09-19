#1)Variables
#1.Create variables to store name, age, and city and display them.
name=input("Enter Name: ")
age=input("Enter Age: ")
city=input("Enter City: ")

print("Name:",name)
print("Age:",name)
print("City:",name)
print("---------------------------------")

#2. Swap the values of two variables.
a=int(input("Enter Number A: "))
b=int(input("Enter Number B: "))
print("Before Swap:",name)
print(a,b)

c=a
a=b
b=c
print("After swap:",name)
print(a,b)
print("---------------------------------")

#3. Calculate the area of a rectangle using variables.
l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
print("Area of rectangle:",l*b)
print("---------------------------------")

#4. Calculate simple interest using variables.
p=int(input("Enter principal: "))
r=int(input("Enter rate: "))
t=int(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)
print("---------------------------------")

#5. Convert Celsius temperature to Fahrenheit.
c=int(input("Enter celsius: "))
f= (c * 9 / 5) + 32
print("Fahrenheit:", f)
