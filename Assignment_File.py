
from datetime import datetime
import os

temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        return f

	
myfile = open("output.txt","w")
for t in temperatures:
   out = c_to_f(t)
   if type(out) != str :
	   myfile.write(str(out)+"\n")
myfile.close()

myfile = open("output.txt")
myfile.seek(0)
print(myfile.read())
myfile.close()


files = ["file1.txt","file2.txt","file3.txt"]
filepath = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"
def merge(filename , filepath):
	with open(filepath,"a+") as myfile :
		filetobeMergerd = open(filename)
		content = filetobeMergerd.read()
		myfile.write(content)
		filetobeMergerd.close()

	
for i in files:
	merge(i,filepath)

	
myfile = open("mergedFile.txt")
myfile.seek(0)
print(myfile.read())
myfile.close()


