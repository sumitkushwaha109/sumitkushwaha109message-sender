import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params = {
        'authorization':'1x7gdAwOeHSGYFE9J3Ks5fqUrWkaXNyBZltjivQPmpDuRnV6ILpYNF3kWVRsMl2ZoLwIuc91KyUDfGCH',
        'sender_id': 'TXTIND',
        'message':message,
        'language': 'english',
        'route': 'v3',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')


def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)
    if r:
        showinfo("Send Success", "Successfully sent")
    else:
        showerror("Error", "Something went wrong..")


# Creating GUI
root = Tk()
root.title("Your Message Sender Box ")
root.geometry("400x550")
font = ("FontSugarfoot", 35, "bold")
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root, text="SEND SMS", command=btn_click)
sendBtn.pack()
root.mainloop()