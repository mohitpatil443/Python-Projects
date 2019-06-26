from tkinter import *
alphabets = "abcdefghijklmnopqrstuvwxyz"
key = 4


def encrypt(word):
    result = ''
    for char in word:
        if char == ' ':
            result += ' '
            continue
        else:
            pos = alphabets.find(char)
            newpos = (pos+key) % 26
            result += alphabets[newpos]
    clearm()
    op.insert(0, result)


def decrypt(word):
    result = ' '
    for char in word:
        if char == ' ':
            result += ' '
            continue
        else:
            pos = alphabets.find(char)
            newpos = (pos-key) % 26
            result += alphabets[newpos]
    clearm()
    op.insert(0, result)


top = Tk()
top.geometry('350x200')
top.title("Encryption")

process = StringVar()
enc = Radiobutton(top, text="Encrypt", value="enc", variable="process")
enc.grid(column=0, row=0)
dec = Radiobutton(top, text="Decrypt", value="dec", variable="process")
dec.grid(column=1, row=0)
inpL = Label(top, text="Input : ").grid(column=0, row=1)

inp = Entry(top, width=20)
inp.grid(column=1, row=1, pady=10)


def clear():
    inp.delete(0, END)
    op.delete(0, END)


def clearm():
    inp.delete(0, END)
    op.delete(0, END)


clear = Button(top, text="Clear", command=clear, bg="red", fg="white")
clear.grid(column=2, row=1, padx=10)

opL = Label(top, text="Output : ")
opL.grid(column=0, row=2)

op = Entry(top, width=20)
op.grid(column=1, row=2, pady=10)


def decide():
    run = enc.getvar("process")
    if run == "enc":
        encrypt(inp.get())

    else:
        decrypt(inp.get())


action = Button(top, text="Process", bg="red", fg="white", command=decide).grid(column=1, row=3, pady=10)


top.mainloop()










