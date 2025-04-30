import tkinter as tk

palavra = "python"
tentativas = 6
letras_corretas = ['_'] * len(palavra)

def adivinhar():
    global tentativas
    letra = entry.get().lower()
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_corretas[i] = letra
        label_palavra.config(text=" ".join(letras_corretas))
    else:
        tentativas -= 1
        label_tentativas.config(text=f"Tentativas restantes: {tentativas}")
    
    if "_" not in letras_corretas:
        label_tentativas.config(text="Você ganhou!")

root = tk.Tk()
root.title("Jogo da Forca")

label_palavra = tk.Label(root, text=" ".join(letras_corretas), font=("Arial", 24))
label_palavra.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Adivinhar", font=("Arial", 14), command=adivinhar)
button.pack(pady=10)

label_tentativas = tk.Label(root, text=f"Tentativas restantes: {tentativas}", font=("Arial", 14))
label_tentativas.pack(pady=10)

root.mainloop()
