def string_length(mystring):
    if type(int(mystring)) == int:
        return "Sorry, integers don't have length"
    elif type(float(mystring)) == float:
        return "Sorry, floats don't have length"
    else:
        return len(mystring)


word = input("Type a word :")
print(string_length(word))
