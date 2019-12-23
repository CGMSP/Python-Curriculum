# Python-Curriculum
The python curriculum for the Activity

## Contents:
- print
- variables
- Data Types
- User input
- Lists
- Functions

## print
print: Print something to the terminal.
syntax:
print()
You can print strings, variables, and other types of data.
#### Example:
`print("Hello World!")`

## variables
Variables are like in math. In python, variables can change throughout the program. This is called "Mutability".
#### Example:
```
x = 10
print('My variable, x is', x) #Print the string 'My variable, x is', and than print the value of x.

var = True

if var == True:
	print('My var is true!')
else:
	print('My var is false')

```
### Data Types
Variables can be many different types of values. For example, "Hello", would be called a string. A string is text. Strings have a type called str. Another type of value is called an integer. Like in math, an integer is a whole number or it's opposite. It's data type is called int. A float, can be any rational number. A Boolean, (type bool) is a value in Boolean logic. These are, for example, True, and False. There are also Boolean operators, (like and, or, xor) which we will get to later.

#### Example:
```
x = 5 # Define x
if type(x) == bool: # If x has the data type of Boolean, than
	print('x has a Boolian value of: ', str(x)) # print a string, and x converted to a string.
elif type(x) == int:  # If x has the data type of an interger:
	print('the type of x is an integer with a value of:', str(x)) # Print that.
elif type(x) == float: #If it's a float:
	print('the type of x is a float with the value of ', str(x))
elif type(x) == str: # Or a string.
	print('the type of x is a string with the value of ', x)
else:
	print('oops')

```


## User Input
User input in python is done with a function called, you guessed it, input. you can define a variable to a prompt.

#### Example:

```
name = input("What is your name?    ") # Define a variable called name to the input from a prompt 'What is your name?'

age = input("How old are you?   ") # Define a variable called age to the input from a prompt 'What is your name?'

print("Your name is ", name, "and you are ", age, "years old") # Print these variables

```
