import tkinter as tk

def enviar():
    texto_usuario = entry_usuario.get()
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, f"Você: {texto_usuario}\n")
    text_area.insert(tk.END, "Bot: Olá, como posso ajudar?\n")
    text_area.config(state=tk.DISABLED)
    entry_usuario.delete(0, tk.END)

root = tk.Tk()
root.title("Aplicativo de Conversa")

text_area = tk.Text(root, height=15, width=50, state=tk.DISABLED, font=("Arial", 12))
text_area.pack(pady=10)

entry_usuario = tk.Entry(root, font=("Arial", 14))
entry_usuario.pack(pady=10)

button_enviar = tk.Button(root, text="Enviar", font=("Arial", 14), command=enviar)
button_enviar.pack(pady=10)

root.mainloop()
