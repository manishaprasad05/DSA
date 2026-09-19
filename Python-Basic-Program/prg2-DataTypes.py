
#2) Data Types
#1. Demonstrate int, float, str, bool, and complex.
a = 10
b = 10.5
name = "Python"
x = True

print(a, type(a))
print(b, type(b))
print(name, type(name))
print(x, type(x))
print("---------------------------------")

#2. Accept two numbers and display their data types.
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("First value:", num1)
print("Data type:", type(num1))
print("Second value:", num2)
print("Data type:", type(num2))
print("---------------------------------")

#3. Convert a string number into an integer and float.
num = "25"
int_num = int(num)
float_num = float(num)
print("Integer:", int_num)
print("Float:", float_num)
print("---------------------------------")

#4. Find the length of a string.
text = "Python"
print("Length of string:", len(text))
print("---------------------------------")

#5. Create a list, tuple, set, and dictionary and display their types.
mylist = [1,2,3,4,5]
mytuple = (1,2,3)
myset = {1,2,3,4,5,6,7}
mydict = {"name": "Manisha", "age": 21}

print(mylist,type(mylist))
print(mytuple,type(mytuple))
print(myset,type(myset))
print(mydict,type(mydict))
