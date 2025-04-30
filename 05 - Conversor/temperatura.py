import tkinter as tk

def converter():
    celsius = float(entry_celsius.get())
    fahrenheit = (celsius * 9/5) + 32
    label_resultado.config(text=f"{fahrenheit} °F")

root = tk.Tk()
root.title("Conversor de Temperatura")

label = tk.Label(root, text="Digite a temperatura em Celsius", font=("Arial", 14))
label.pack(pady=10)

entry_celsius = tk.Entry(root, font=("Arial", 14))
entry_celsius.pack(pady=10)

button = tk.Button(root, text="Converter", font=("Arial", 14), command=converter)
button.pack(pady=10)

label_resultado = tk.Label(root, font=("Arial", 14))
label_resultado.pack(pady=10)

root.mainloop()
