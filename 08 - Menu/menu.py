import tkinter as tk
from tkinter import messagebox

def nova_acao():
    messagebox.showinfo("Nova Ação", "Ação criada com sucesso!")

root = tk.Tk()
root.title("Menu Personalizado")

menu = tk.Menu(root)
root.config(menu=menu)

arquivo_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Arquivo", menu=arquivo_menu)
arquivo_menu.add_command(label="Nova", command=nova_acao)
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=root.quit)

root.mainloop()
