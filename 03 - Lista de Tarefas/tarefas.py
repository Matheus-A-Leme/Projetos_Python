import tkinter as tk

def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa != "":
        listbox.insert(tk.END, tarefa)
        entry_tarefa.delete(0, tk.END)

def remover_tarefa():
    try:
        selecionado = listbox.curselection()
        listbox.delete(selecionado)
    except:
        pass

root = tk.Tk()
root.title("To-Do List")

entry_tarefa = tk.Entry(root, font=("Arial", 14))
entry_tarefa.pack(pady=10)

button_adicionar = tk.Button(root, text="Adicionar", font=("Arial", 14), command=adicionar_tarefa)
button_adicionar.pack()

listbox = tk.Listbox(root, font=("Arial", 14), height=10, width=40)
listbox.pack(pady=10)

button_remover = tk.Button(root, text="Remover", font=("Arial", 14), command=remover_tarefa)
button_remover.pack()

root.mainloop()
