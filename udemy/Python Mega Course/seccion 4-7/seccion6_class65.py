with open("example59.txt",'a+') as file:
    #file.seek(0)
    content = file.read()
    file.write("\nLine 8")
