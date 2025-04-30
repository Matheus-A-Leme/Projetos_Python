import tkinter as tk

def clicar(botoes):
    entry_text.set(entry_text.get() + botoes)

def calcular():
    try:
        resultado = eval(entry_text.get())
        entry_text.set(resultado)
    except:
        entry_text.set("Erro")

def limpar():
    entry_text.set("")

root = tk.Tk()
root.title("Calculadora Simples")

entry_text = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), bd=10, relief="sunken", width=15, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 20), command=calcular, height=2, width=4)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 20), command=limpar, height=2, width=4)
    else:
        button = tk.Button(root, text=text, font=("Arial", 20), command=lambda b=text: clicar(b), height=2, width=4)
    button.grid(row=row, column=col)

root.mainloop()
