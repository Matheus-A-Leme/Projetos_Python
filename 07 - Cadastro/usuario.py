import tkinter as tk

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    print(f"Usuário cadastrado: {nome}, {email}, {senha}")
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_senha.delete(0, tk.END)

root = tk.Tk()
root.title("Cadastro de Usuário")

label_nome = tk.Label(root, text="Nome", font=("Arial", 14))
label_nome.pack(pady=5)

entry_nome = tk.Entry(root, font=("Arial", 14))
entry_nome.pack(pady=5)

label_email = tk.Label(root, text="Email", font=("Arial", 14))
label_email.pack(pady=5)

entry_email = tk.Entry(root, font=("Arial", 14))
entry_email.pack(pady=5)

label_senha = tk.Label(root, text="Senha", font=("Arial", 14))
label_senha.pack(pady=5)

entry_senha = tk.Entry(root, font=("Arial", 14), show="*")
entry_senha.pack(pady=5)

button_cadastrar = tk.Button(root, text="Cadastrar", font=("Arial", 14), command=cadastrar)
button_cadastrar.pack(pady=10)

root.mainloop()
