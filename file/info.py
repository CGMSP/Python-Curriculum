import sys
import os
filename = input("What would you like your file to be called?   ")
writefile = open(filename, "w+")

name = input("What is your name?    ")
age = input("how old are you?   ")
info = [name, age]

writefile.write(str(name))
writefile.write(', ')
writefile.write(str(age))


writefile.close()
