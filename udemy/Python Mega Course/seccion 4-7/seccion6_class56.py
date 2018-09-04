# Please download the text file from the attachment.
# Then write some code that reads the content of the file generates the
# following output in the command line:


file = open("fruits.txt", "r")
content = file.readlines()
file.close()
for i in content:
     print(i.strip("\n"))
