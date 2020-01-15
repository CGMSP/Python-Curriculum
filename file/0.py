import sys
import os
cwd = os.getcwd()
path = "files"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


filename = 'files/yourprogram'
writefile = open(filename, "w+")

writefile.write("the current working directory is:")
writefile.write(cwd)
writefile.write("\r\n")


for i in range(10):
      writefile.write("This is line %d\r\n" % (i+1))

writefile.close()
