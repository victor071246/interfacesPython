from tkinter import Tk, Label, PhotoImage

root = Tk()
photo = PhotoImage(file='computer2.gif') #.subsample(5)
hello = Label (master=root, image=photo, width=300, height=180) #text='Olá classe!'
hello.pack()
root.mainloop()
