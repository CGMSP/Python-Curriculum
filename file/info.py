import sys
import os
cwd = os.getcwd()
path = "files"
filename = 'files/info.csv'
writefile = open(filename, "w+")

try:
    os.mkdir(path)
except OSError:
    print ("The directory %s already exists" % path)
else:
    print ("Successfully created the directory %s " % path)


name = input("What is your name?    ")
age = input("how old are you?   ")
info = [name, age]


with open(filename, 'a') as filehandle:
    for listitem in info:
        filehandle.write('%s\n' % listitem)



writefile.close()
