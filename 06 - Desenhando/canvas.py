import tkinter as tk

def desenhar(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=2)

root = tk.Tk()
root.title("Desenhando no Canvas")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

canvas.bind("<B1-Motion>", desenhar)

root.mainloop()
