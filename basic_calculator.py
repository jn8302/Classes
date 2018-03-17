from tkinter import *
from tkinter import ttk

root = Tk()

Label(root, text= "Calculator").grid(row = 0)

e1 = Entry(root)

e1.grid(row=1,columnspan = 4)

b7 = Button(root, text = "7").grid(row = 2,column = 1)
b8 = Button(root, text = "8").grid(row = 2,column = 2)
b9 = Button(root, text = "9").grid(row = 2,column = 3)

b4 = Button(root, text = "4").grid(row = 3,column = 1)
b5 = Button(root, text = "5").grid(row = 3,column = 2)
b6 = Button(root, text = "6").grid(row = 3,column = 3)

b1 = Button(root, text = "1").grid(row = 4,column = 1)
b2 = Button(root, text = "2").grid(row = 4,column = 2)
b3 = Button(root, text = "3").grid(row = 4,column = 3)


def add_2_num(n1,n2):
    return n1 + n2
    

def sub_2_num(n1,n2):
    return n1-n2

n1 = ""

"""
while True:
    if n1 == "":
        n1 = int(input(" enter number: ")) 
    op = input(" enter and operator")
    n2 = int(input(" enter number: "))
    if(op == "+"):
        n1 = add_2_num(n1,n2)
        print(n1)
"""

if __name__ == "__main__":
    main()



root.mainloop()
