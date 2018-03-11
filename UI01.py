import tkinter as tk

counter = 0
def counterLabel(label):
    def count():
        global counter
        counter += 1
        label.config(text = str(counter))
        label.after(1000,count)
    count()

def resetCounter():
    #print("Reset")
    #label.config(text = "0")

    global counter
    counter = 0

# main window

root = tk.Tk()



root.title("Da Bomb")

label = tk.Label(root, fg = "green")
label.pack()
counterLabel(label)


logo = tk.PhotoImage(file = "assets/python_logo.png")

w1 = tk.Label(root, image=logo).pack(side="left")
labelText = "This calculator is da bomb"
w = tk.Label(root, text = labelText)
w.pack()


button = tk.Button(root, text = "Reset", width=25, command = resetCounter)
button.pack()
root.mainloop()
