from engine.request import post
from engine.messenger import main as mess
from tkinter import *
from tkinter import messagebox


def main():
    window = Tk()
    email = StringVar()
    password = StringVar()

    def login():
        if len(email.get()) != 0:
            if len(password.get()) != 0:
                response = post({"method": "login", "email": email.get().strip(), "pass": password.get().strip()})
                if "error" not in str(response):
                    window.destroy()
                    mess(response["response"])
                else:
                    messagebox.showinfo("Осторожно", "Либо email, либо пароль не верный.")

            else:
                messagebox.showinfo("Я вижу только пустоту", "Пожалуйста введите пароль")
        else:
            messagebox.showinfo("О нет, меня встречает пустота", "Пожалуйста введите email")

    window.title("Вход")
    window.geometry("400x250")
    label = Label(window, text="Ваш email:")
    label.grid(column=0, row=0)
    entry = Entry(window, width=20, textvariable=email)
    entry.grid(column=1, row=0)
    label_ni = Label(window, text="Ваш пароль:")
    label_ni.grid(column=0, row=1)
    entry_hi = Entry(window, width=20, textvariable=password)
    entry_hi.grid(column=1, row=1)
    button = Button(window, text="Готово", command=login)
    button.grid(column=2, row=1)
    window.mainloop()