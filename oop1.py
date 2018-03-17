from tkinter import *

class Calculator(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)
        self.createElements()

    def createElements(self):
        self.display = Entry(self, font=("Arial", 16), relief=RAISED,
                             justify=RIGHT)
        self.display.insert(0,"0")
        self.display.grid(row=0,column=0,columnspan=4)

        #top row
        self.b7 = Button(self,font=("Arial",11),text ="7")
        self.b7.grid(row=1,column=0, sticky=NSEW)
        self.b8 = Button(self,font=("Arial",11),text ="8")
        self.b8.grid(row=1,column=1, sticky=NSEW)
        self.b9 = Button(self,font=("Arial",11),text ="9")
        self.b9.grid(row=1,column=2, sticky=NSEW)
        self.ba = Button(self,font=("Arial",11),text ="+")
        self.ba.grid(row=1,column=3, sticky=NSEW)

        #mid row
        self.b4 = Button(self,font=("Arial",11),text ="4")
        self.b4.grid(row=2,column=0, sticky=NSEW)
        self.b5 = Button(self,font=("Arial",11),text ="5")
        self.b5.grid(row=2,column=1, sticky=NSEW)
        self.b6 = Button(self,font=("Arial",11),text ="6")
        self.b6.grid(row=2,column=2, sticky=NSEW)
        self.bs = Button(self,font=("Arial",11),text ="-")
        self.bs.grid(row=2,column=3, sticky=NSEW)

        #bottom row
        self.b1 = Button(self,font=("Arial",11),text ="1")
        self.b1.grid(row=3,column=0, sticky=NSEW)
        self.b2 = Button(self,font=("Arial",11),text ="2")
        self.b2.grid(row=3,column=1, sticky=NSEW)
        self.b3 = Button(self,font=("Arial",11),text ="3")
        self.b3.grid(row=3,column=2, sticky=NSEW)
        self.bm = Button(self,font=("Arial",11),text ="x")
        self.bm.grid(row=3,column=3, sticky=NSEW)

        self.b0 = Button(self,font=("Arial",11),text ="0")
        self.b0.grid(row=4,column=0, columnspan = 2,sticky=NSEW)
        self.bc = Button(self,font=("Arial",11),text ="c")
        self.bc.grid(row=4,column=2, sticky=NSEW)
        self.be = Button(self,font=("Arial",11),text ="=")
        self.be.grid(row=4,column=3, sticky=NSEW)
def main():
    """Main Function."""
    root = Tk()
    root.title("Frame__1")
    root.resizable(1, 0)
    app = Calculator(root)
    app.grid()
    
    root.mainloop()












if (__name__ == '__main__'):
    main()
