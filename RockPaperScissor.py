from tkinter import *
import random

usr = 0
comp = 0


def restart():
    global usr, comp, b4
    usr=comp=0
    b4.grid_forget()
    l2.config(text='max points = 5', font=('Verdana', 12), bg='Gray20', fg='Gray69', pady=40)
    l3.config(text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20',
                  fg='Gray69')
    l1.grid(column=0, row=0, columnspan=6)
    l2.grid(column=0, row=1, columnspan=6)
    b1.grid(column=0, row=5, columnspan=2)
    b2.grid(column=2, row=5, columnspan=2)
    b3.grid(column=4, row=5, columnspan=2)
    l3.grid(column=0, row=7, columnspan=6)


def rock():
    global usr, comp, l2, l3, b1, b2, b3
    c = random.randint(1, 4)
    if c == 1:
        l2.config(font=('Verdana', 11, 'bold'), bg="gray20", fg="white",
            text="\nUser's move: Rock\t\t\tComputer's move: Rock\n\n\nTIE!!\n")
        l3.config(text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20',
                  fg='Gray69')
    elif c == 2:
        comp+=1
        l2.config(font=('Verdana', 11, 'bold'), bg="gray20", fg="white",
           text="\nUser's move: Rock\t\t\tComputer's move: Paper\n\n\nComputer gets a point.\n")
        l3.config(text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20',
                  fg='Gray69')
    elif c == 3:
        usr+=1
        l2.config(font=('Verdana', 11, 'bold'), bg="gray20", fg="white",
                  text="\nUser's move: Rock\t\t\tComputer's move: Scissor\n\n\nUser gets a point.\n")
        l3.config(text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20',
                  fg='Gray69')
    if usr == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        l2.configure(font=('Segoe Script', 16, 'bold'), bg="gray20", fg="Cyan",
                      text="\nUser wins!!\nCongratulations!!\n")
        b4.grid(column=2, row=8, columnspan=2)
    elif comp == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        l2.configure(font=('Segoe Script', 16, 'bold'), bg="gray20", fg="Cyan",
                      text="\nComputer wins!!\nBetter Luck Next time!!\n")
        b4.grid(column=2, row=8, columnspan=2)


def paper():
    global usr, comp, l2, l3, b1, b2, b3
    c = random.randint(1, 4)
    if c == 1:
        usr+=1
        l2.config(font=('Verdana', 11, 'bold'), bg="gray20", fg="white",
            text="\nUser's move: Paper\t\t\tComputer's move: Rock\n\n\nUser gets a point.\n")
        l3.config(text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20',
                  fg='Gray69')
    elif c == 2:
        l2.config(font=('Verdana', 11, 'bold'), bg="gray20", fg="white",
           text="\nUser's move: Paper\t\t\tComputer's move: Paper\n\n\nTIE!!\n")
        l3.config(text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20',
                  fg='Gray69')
    elif c == 3:
        comp+=1
        l2.config(font=('Verdana', 11, 'bold'), bg="gray20", fg="white",
                  text="\nUser's move: Paper\t\t\tComputer's move: Scissor\n\n\nComputer gets a point.\n")
        l3.config(text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20',
                  fg='Gray69')
    if usr == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        l2.configure(font=('Segoe Script', 16, 'bold'), bg="gray20", fg="Cyan",
                      text="\nUser wins!!\nCongratulations!!\n")
        b4.grid(column=2, row=8, columnspan=2)
    elif comp == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        l2.configure(font=('Segoe Script', 16, 'bold'), bg="gray20", fg="Cyan",
                      text="\nComputer wins!!\nBetter Luck Next time!!\n")
        b4.grid(column=2, row=8, columnspan=2)


def scissor():
    global usr, comp, l2, l3, b1, b2, b3
    c = random.randint(1, 4)
    if c == 1:
        comp+=1
        l2.config(font=('Verdana', 11, 'bold'), bg="gray20", fg="white",
            text="\nUser's move: Scissor\t\t\tComputer's move: Rock\n\n\nComputer gets a point.\n")
        l3.config(text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20',
                  fg='Gray69')
    elif c == 2:
        usr+=1
        l2.config(font=('Verdana', 11, 'bold'), bg="gray20", fg="white",
           text="\nUser's move: Scissor\t\t\tComputer's move: Paper\n\n\nUser gets a point.\n")
        l3.config(text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20',
                  fg='Gray69')
    elif c == 3:
        l2.config(font=('Verdana', 11, 'bold'), bg="gray20", fg="white",
                  text="\nUser's move: Scissor\t\t\tComputer's move: Scissor\n\n\nTIE!!\n")
        l3.config(text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20',
                  fg='Gray69')
    if usr == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        l2.configure(font=('Segoe Script', 16, 'bold'), bg="gray20", fg="Cyan",
                      text="\nUser wins!!\nCongratulations!!\n")
        b4.grid(column=2, row=8, columnspan=2)
    elif comp == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        l2.configure(font=('Segoe Script', 16, 'bold'), bg="gray20", fg="Cyan",
                      text="\nComputer wins!!\nBetter Luck Next time!!\n")
        b4.grid(column=2, row=8, columnspan=2)


am = Tk()
am.geometry('600x500')
am.title('RPS x Game')
am.config(bg='Gray20')
am.resizable(height=False, width=False)
l1 = Label(am, text='ROCK PAPER SCISSOR', font=('Segoe UI Black', 25), bg='Gray20', fg='Gray69', pady=20)
l2 = Label(am, text='max points = 5', font=('Verdana', 12), bg='Gray20', fg='Gray69', pady=40)
b1 = Button(am, text="ROCK", font=('Verdana', 12), height=6, width=12, bg='black', fg='Gray69',
            bd=0, activebackground='brown', activeforeground='white', command=rock)
b2 = Button(am, text="PAPER", font=('Verdana', 12), height=6, width=12, bg='black', fg='Gray69',
            bd=0, activebackground='green', activeforeground='black', command=paper)
b3 = Button(am, text="SCISSOR", font=('Verdana', 12), height=6, width=12, bg='black', fg='Gray69',
            bd=0, activebackground='turquoise1', activeforeground='black', command=scissor)
b4 = Button(am, text="RESTART", font=('Verdana', 12), width=10, bg='black', fg='Gray69',
            bd=0, activebackground='gray40', activeforeground='white', command=restart)
l3 = Label(am, text=f'User Score={usr}\t\t\t\t Computer Score={comp}', font=('Verdana', 12), bg='Gray20', fg='Gray69', pady=50)
l1.grid(column=0, row=0, columnspan=6)
l2.grid(column=0, row=1, columnspan=6)
b1.grid(column=0, row=5, columnspan=2)
b2.grid(column=2, row=5, columnspan=2)
b3.grid(column=4, row=5, columnspan=2)
l3.grid(column=0, row=7, columnspan=6)


am.grid_rowconfigure(0, weight=1)
am.grid_rowconfigure(1, weight=1)
am.grid_rowconfigure(2, weight=1)
am.grid_rowconfigure(3, weight=1)
am.grid_rowconfigure(4, weight=1)
am.grid_rowconfigure(5, weight=1)
am.grid_rowconfigure(6, weight=1)
am.grid_rowconfigure(7, weight=1)
am.grid_rowconfigure(8, weight=1)
am.grid_columnconfigure(0, weight=1)
am.grid_columnconfigure(1, weight=1)
am.grid_columnconfigure(2, weight=1)
am.grid_columnconfigure(3, weight=1)
am.grid_columnconfigure(4, weight=1)
am.grid_columnconfigure(5, weight=1)

am.mainloop()
#Akhil