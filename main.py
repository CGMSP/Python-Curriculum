# Print
print('Hello World')

# Vars
Myvar = 'This is in a variable'
print(Myvar)

#Extension:
# print a string along with a variable

x = 10
print('My variable, x is', x)


var = True

if var == True:
	print('My var is true!')
else:
	print('My var is false')

# Data types

x = 5
if type(x) == bool:
	print('x has a boolian value of: ', str(x))
elif type(x) == int:
	print('the type of x is an integer with a value of:', str(x))
elif type(x) == float:
	print('the type of x is a float with the value of ', str(x))
elif type(x) == str:
	print('the type of x is a string with the value of ', x)
else:
	print('oops')

# User input:
name = input("What is your name?    ")
age = input("How old are you?   ")

print("Your name is ", name, "and you are ", age, "years old")

# Lists

name = input("What is your name?    ")
age = input("How old are you?   ")
info = [name, age]
selection = input("If you would like to see your name, type 0. Of you would like to know your age, type 1.")

print(info[int(selection)])

# Functions
## Without params
def my_function():
    return "Im in a function!"

print(my_function())

## With params
y = False
def new_function(y):
    return type(y), y
    print(new_function(y))
