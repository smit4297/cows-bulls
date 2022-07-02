from tkinter import *


ws = Tk()
ws.geometry('600x380')
ws.title('Cows & Bulls Game')
ws['bg'] = '#5d8a82'
f = ("Times bold", 14)

img = PhotoImage(file="cowsbulls.png")


def next_page():
    ws.destroy()
    # import rulespage


def prev_page():
    ws.destroy()
    # import page3


Label(
    ws,
    text="Welcome To Cows & Bulls Game",
    image=img,
    padx=20,
    pady=20,
    font=f
).pack(expand=True, fill=BOTH)


Button(
    ws,
    text="Rules",
    font=f,
    command=prev_page
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
