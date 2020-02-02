# Python-Curriculum
The python curriculum for the Activity

## Contents:
- Print
- Variables
- Data Types
- User input
- Lists
- Functions

## Print
print(): Print something to the terminal.
syntax:
print()
You can print strings, variables, and other types of data.
#### Example:
`print("Hello World!")`

## Variables
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


## Conditional Statements
Conditional statements are at the heart of programming. In essence, it is simply saying "if this, than that."
#### Example:
```
var = True # Define variable 'var'

if var == True: #If it's true ...
	print('My var is true!') # Print that to the terminal
elif var == False: # If it's false...
	print('My var is false') # Print that to the terminal
else:
  print("Your var could be of a different data type, which you will learn about in the next section.")
```

## Data Types
Variables can be many different types of values. For example, "Hello", would be called a string. A string is text (eg. “hello world”). Strings have a type called str. Another type of value is called an integer. Like in math, an integer is a whole number or it's opposite (eg. 5). It's data type is called int. A float, can be any rational number (eg. 5.2). A Boolean, (type bool) is a value in Boolean logic (eg. True). These are, for example, True, and False. There are also Boolean operators, (like and, or, xor) which we will get to later.


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

## Lists
Lists are lists. They are variables that contain a list of things.
#### Examples
```
name = input("What is your name?    ")
age = input("How old are you?   ")
info = [name, age] # define a list called 'info' with the users name and age.
selection = input("If you would like to see your name, type 0. Of you would like to know your age, type 1.") # Make a var called 'selection' which is the response to the prompt :"If you would like to see your name, type 0. Of you would like to know your age, type 1."
if int(selection) < 2: # If the selection is 1 or 0 (if it is valid)
	print(info[int(selection)]) # print the selection'th entry in the list called 'info'
else: # if the selection is not legal (more than 2)
    raise RuntimeError('Wrong Argument. Please enter a selection of 1 or 0.')
```

## Functions
Functions are blocks of code. When you 'call' a function, you are essentially running all of the code that is inside of the function. Functions can have parameters, or 'arguments'. If you have a function with parameters, you can tell the function to compute something about the parameters.

#### Examples
```
def my_function():
    return "I'm in a function!"
print(my_function()) # Will print "Im in a function!"
```

## Loops
Loops are used to do something multiple times. You can choose to repeat code *while* a condition is true or false. You can also choose to repeat code *for* every time a variable goes into another variable or a range.
#### Examples
##### For
Variable into variable:
```
z = 10
while z > 0: #While z is less than 10
	print("z is ", z) # print the value of z
	z -= 1 # z = z - 1

```
Do it 10 times (range)

```

for i in range(10):
	print("this will happen 10 times")

```
##### While
```
fruits = ['apple', 'banana', 'pomegranate'] # Define a list of fruits
i = 0
x = 0
for i in fruits: # For every time i goes into fruits (this is 3 times)
	print(fruits[x]) # print the Xth item in the list 'fruits'
	x = x + 1 # Add 1 to x
```

## Math stuff

### Operations


#### Addition & Subtraction
Addition and subtraction are quite simple. It's simply plus and minus.

##### Example    

```     
x = 5        
x == x + 1                                    
print(x) # This will print X which is now 6.            
x += 1 # += is adds the following amount                
print(x) # prints X which is now 7                  



```                    



#### Multiplication                            
Multiplication uses the * (asterisk) symbol.                      
##### Example                    
```                          
x = 5 # x is 5                     
print(x) # prints x which is 5                  
x = x * 3 # x is now x (5) * 3 (15)           
print(x) # prints x which is now 15        
x *= 2 # multiplies x by 2              
print(x) # prints x which is now 30              
```                      
               
#### Division                 
In python, there are 2 types of division. One that actually divides the two numbers, and one that returns the remainder.              
#### Example                      
This is an example of the first type of division in python.            
```             
x = 5 # x is 5                 
print(x) # prints x which is 5         
x = x / 5 # divides x by 5        
print(x) # prints x which is now 1.            
x /= 2 # divides x by 2                
print(x) # prints x which is now 0.5            
```            

#### Exponents                                       
In python, exponents are handled using two asterisks.                  

##### Example

```
x = 2 # x is 2
print(x) # prints x which is now 2
x = x ** 2 
print(x) # prints x which is now 2 squared, or 4.
x **= 2 
print(x) # prints x which is now 16      



```
