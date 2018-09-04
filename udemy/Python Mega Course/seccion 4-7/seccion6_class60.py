# Please create some code creates a text file and writes the items of list
# numbers = [1, 2, 3] to that text file.

file = open("seccion6_class60_txt",'w')
numbers = [1,2,3]
for i in numbers:
    file.write(str(i)+"\n")

file.close()
