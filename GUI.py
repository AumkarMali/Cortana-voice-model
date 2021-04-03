from tkinter import *
import tkinter
from subprocess import call
import tkinter as tk
import tkinter.font as font

def gui(data):
    window = Tk()
    window.title("Cortana")
    window.configure(background='#0066cc')
    window.geometry('1000x700')
    myFont = font.Font(family='Helvetica', size=10, weight='bold')
    text_font = font.Font(family='Cambria', size=40)


    lbl = Label(window, text="Cortana", bg='#0066cc', font=("Cambria", 50))
    lbl.pack()

    def update_btn_text():
        btn_text.set("DISCORD BOT ACTIVATED")

    btn_text = tk.StringVar()
    btn = tk.Button(window, textvariable=btn_text, command=update_btn_text, bg='#44D554', width=30, height=2).place(x=765, y=140)
    btn_text.set("ACTIVATE DISCORD BOT")

    get_question = tk.StringVar()
    Questions = Label(window, textvariable=get_question, bg='#0066cc', font=("Cambria", 20)).place(x=0, y=140)
    get_question.set("Speech: " + data)

    window.mainloop()

