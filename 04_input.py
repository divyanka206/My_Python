# input() is a function
# it is used to take and store the value from the user
# by default it stores the value in str data type

name = input("enter name: ")
print(name)

# to change the data type of the value we do type casting

name = input("enter name: ")
age = int(input("enter age: "))   #type casting str to int
marks = int(input("enter marks: "))
print("Welcome", name)
print("Age", age)
print("Marks", marks)
