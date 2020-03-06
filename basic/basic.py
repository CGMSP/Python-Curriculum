# Print
print('Hello World')

# Vars
Myvar = 'This is in a variable'
print(Myvar)

#Extension:
# print a string along with a variable

x = 10
print('My variable, x is', x)

#Conditional Statements
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
if int(selection) < 2:
	print(info[int(selection)])
else:
    raise RuntimeError('Wrong Argument. Please enter a selection of 1 or 0.')
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


# loops
## while

z = 10
while z > 0:
	print("z is ", z)
	z -= 1 # z = z - 1

#for
fruits = ['apple', 'banana', 'pomegranate']
i = 0
x = 0
for i in fruits:
	print(fruits[x])
	x = x + 1

# For with range

for i in range(10):
	print("this will happen 10 times")

# Boolean operators
x = True
y = False
if x is y:
	print("X and y are the same")
elif x is not y:
	print("X and y are not equal.")
else:
	raise RuntimeError("Gottem good")
