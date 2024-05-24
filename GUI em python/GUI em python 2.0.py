from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='computer2.gif') #.subsample(5)
image = Label (master=root, image=photo, width=300, height=180) #text='Olá classe!'
image.pack(side=TOP)
text = Label(master=root, font=('Courier', 18), text='Olá alunos da UNIVESP!')
text.pack(side=BOTTOM)
root.mainloop()
