from engine.request import post
from engine.messenger import main as mess
from tkinter import *
from tkinter import messagebox


def main():
    window = Tk()
    text = StringVar()
    code = None
    email = None
    password = None
    last_name = None
    first_name = None

    def namaewa_ni():
        nonlocal first_name, last_name
        if len(text.get()) != 0:
            if len(text.get().split()) >= 2:
                first_name = text.get().split()[0]
                last_name = text.get().split()[1]
            else:
                first_name = text.get().split()[0]
                last_name = 'None'
            params = {"method": "confirm", "email": email, "pass": password, "first_name": first_name,
                      "last_name": last_name}
            response = post(params)
            window.destroy()
            mess(response["response"])
        else:
            messagebox.showinfo("Пустота в моей душе", "Пожалуйста введите имя и фамилию")

    def namaewa():
        nonlocal password
        if len(text.get()) != 0:
            if len(text.get()) > 6:
                password = text.get()
                label.configure(text="Ваше имя и фамилия:")
                text.set("")
                button.configure(command=namaewa_ni)
            else:
                messagebox.showinfo("Слабенький какой-то", "Пароль должен быть длиннее 6 символов!")
        else:
            messagebox.showinfo("Надо бы подумать", "Придумайте пароль!")

    def check_code():
        if len(text.get()) != 0:
            if str(code) == text.get():
                label.configure(text="Придумайте пароль:")
                text.set("")
                button.configure(command=namaewa)
            else:
                messagebox.showinfo("Неправильно", "Не верный код подтверждения!")
        else:
            messagebox.showinfo("Как-то пустовато", "Введите код подтверждения!")

    def reg_code():
        nonlocal email, code
        if len(text.get()) != 0:
            params = {"method": "register", "email": text.get()}
            code = post(params)
            if "error" not in str(code):
                email = text.get()
                code = code["code"]
                label.configure(text="Код подтверждения!")
                text.set("")
                button.configure(command=check_code)
            else:
                messagebox.showinfo("Снова пустовато", "Пожалуйста, введите ваш email!")
        else:
            messagebox.showinfo("Снова пустовато", "Пожалуйста, введите ваш email!")
            text.set("")

    window.title("Регистрация")
    window.geometry("400x250")
    label = Label(window, text="Ваш email:")
    label.grid(column=0, row=0)
    entry = Entry(window, width=20, textvariable=text)
    entry.grid(column=1, row=0)
    button = Button(window, text="Готово", command=reg_code)
    button.grid(column=3, row=0)
    window.mainloop()