import tkinter as tk
import random

def verificar():
    numero = int(entry.get())
    if numero < sorteado:
        label_resposta.config(text="Muito baixo! Tente novamente.")
    elif numero > sorteado:
        label_resposta.config(text="Muito alto! Tente novamente.")
    else:
        label_resposta.config(text="Você acertou!")

sorteado = random.randint(1, 100)

root = tk.Tk()
root.title("Jogo de Adivinhação")

label = tk.Label(root, text="Adivinhe o número entre 1 e 100", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Verificar", font=("Arial", 14), command=verificar)
button.pack(pady=10)

label_resposta = tk.Label(root, font=("Arial", 14))
label_resposta.pack(pady=10)

root.mainloop()
