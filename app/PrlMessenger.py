from engine import register as rg, login as lg
from tkinter import *

window = Tk()


def login():
    window.destroy()
    lg.main()


def register():
    window.destroy()
    rg.main()


window.title("PrlMessenger")
window.resizable(False, False)
window.geometry("300x100")
button = Button(window, text="Вход", command=login, width=7, height=2, bg="lightblue")
button_ni = Button(window, text="Регистрация", command=register, width=10, height=2, bg="lightblue")
button.pack(side=LEFT, expand=1)
button_ni.pack(side=LEFT, expand=1)
window.mainloop()
