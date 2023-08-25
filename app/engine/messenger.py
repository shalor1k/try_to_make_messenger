from engine.request import get
from engine.server import Server
from random import randint as random
from tkinter import *


def crypt_decrypt(message):
    key = 6779
    text = ''
    for i in message:
        text += chr(ord(i) ^ key)
    return text


def main(user_id):
    window = Tk()
    # window.iconbitmap(default="icon.ico")
    text = StringVar()
    window.title("Параллель мессенджер")
    window.geometry("382x530")
    window.resizable(False, False)
    Chat = Text(window, bg="#333333", fg="#ccc")
    Chat.place(x=0, y=0, width=382, height=475)
    server = Server()
    server.get_name()

    def loopupdate():
        Chat.see(END)
        response = server.update()
        try:
            name = "Я" if int(response['update'][0]['peer_id']) == user_id else response['update'][0]['first_name']
            Chat.insert(END, f"{name}: {crypt_decrypt(response['update'][0]['message'])}\n")
        except:
            window.after(1, loopupdate)
            return
        window.after(1, loopupdate)
        return

    def sendproc(event=None):
        if len(text.get()) != 0:
            print("++++++++++++++++++")
            print(f"Отправил сообщение\n"
                  f"Текст: {crypt_decrypt(text.get())}\n"
                  f"От: {user_id}")
            params = {"method": "message", "message": crypt_decrypt(text.get()), "user_id": user_id}
            get(params)
            text.set("")

    def on_quit():
        get({"method": "quit", "client_name": server.client_name})
        window.destroy()

    enter_text = Entry(window, textvariable=text, bg="#333333", fg="#ccc")
    send_message = Button(text='>', width=7, height=3, bg="#333333", fg="#ccc", command=sendproc)
    enter_text.bind('<Return>', sendproc)
    enter_text.focus_set()
    enter_text.place(x=0, y=475, width=323, height=55)
    send_message.place(x=323, y=475)
    window.protocol("WM_DELETE_WINDOW", on_quit)
    window.after(1, loopupdate)
    window.mainloop()
