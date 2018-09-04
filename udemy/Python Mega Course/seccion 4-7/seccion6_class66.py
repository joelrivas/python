# For this exercise, please write the output in a text file instead of printing
# it out in the terminal.

temperatures = [10,-20,-289,100]

def cel_to_far_txt(c):
    with open("seccion6_class66_txt.txt",'w') as file:
        for i in temperatures:
            if i > -273.15:
                f = i * 9/5 + 32
                file.write(str(f)+"\n")

cel_to_far_txt(temperatures)
