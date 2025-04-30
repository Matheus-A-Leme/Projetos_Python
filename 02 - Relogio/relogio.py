import tkinter as tk
import time

def atualizar_hora():
    hora = time.strftime("%H:%M:%S")
    label.config(text=hora)
    label.after(1000, atualizar_hora)

root = tk.Tk()
root.title("Relógio Digital")

label = tk.Label(root, font=("Helvetica", 48), fg="blue", bg="black")
label.pack()

atualizar_hora()
root.mainloop()
