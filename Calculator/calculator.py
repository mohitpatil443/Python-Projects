from tkinter import *

operator = ''


def implement(num):
    global operator
    operator = operator + str(num)
    exp.setvar('operator', operator)


def clear():
    global operator
    operator = ''
    exp.setvar('operator', operator)


def equals():
    global operator
    sumup = eval(operator)
    exp.setvar('operator', sumup)
    operator = ''


top = Tk()
top.title('Calculator')

exp = Entry(top, font=('arial', 20, 'bold'), bd=30, bg="powder blue", textvariable='operator', justify='right')
exp.grid(columnspan=4)


num9 = Button(top, text=9, command=lambda: implement(9), bg="powder blue", padx=20, pady=10)
num9.grid(row=1, column=0)

num8 = Button(top, text=8, command=lambda: implement(8), bg="powder blue", padx=20, pady=10)
num8.grid(row=1, column=1)

num7 = Button(top, text=7, command=lambda: implement(7), bg="powder blue", padx=20, pady=10)
num7.grid(row=1, column=2)

multiply = Button(top, text='X', command=lambda: implement('*'), bg="powder blue", padx=20, pady=10)
multiply.grid(row=1, column=3)

num6 = Button(top, text=6, command=lambda: implement(6), bg="powder blue", padx=20, pady=10)
num6.grid(row=2, column=0)

num5 = Button(top, text=5, command=lambda: implement(5), bg="powder blue", padx=20, pady=10)
num5.grid(row=2, column=1)

num4 = Button(top, text=4, command=lambda: implement(4), bg="powder blue", padx=20, pady=10)
num4.grid(row=2, column=2)

div = Button(top, text='/', command=lambda: implement('/'), bg="powder blue", padx=20, pady=10)
div.grid(row=2, column=3)


num3 = Button(top, text=3, command=lambda: implement(3), bg="powder blue", padx=20, pady=10)
num3.grid(row=3, column=0)

num2 = Button(top, text=2, command=lambda: implement(2), bg="powder blue", padx=20, pady=10)
num2.grid(row=3, column=1)

num1 = Button(top, text=1, command=lambda: implement(1), bg="powder blue", padx=20, pady=10)
num1.grid(row=3, column=2)

sub = Button(top, text='-', command=lambda: implement('-'), bg="powder blue", padx=20, pady=10)
sub.grid(row=3, column=3)

dot = Button(top, text='.', command=lambda: implement('.'), bg="powder blue", padx=20, pady=10)
dot.grid(row=4, column=0)

num0 = Button(top, text=0, command=lambda: implement(0), bg="powder blue", padx=20, pady=10)
num0.grid(row=4, column=1)

add = Button(top, text='+', command=lambda: implement('+'), bg="powder blue", padx=20, pady=10)
add.grid(row=4, column=2)

equ = Button(top, text='=', command=lambda: equals(), bg="powder blue", padx=20, pady=10)
equ.grid(row=4, column=3)

cls = Button(top, text='Clear', command=lambda: clear(), bg="red", fg='white', padx=20, pady=10)
cls.grid(row=5, column=3)


top.mainloop()
