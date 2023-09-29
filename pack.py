from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("550x780")

btn = ttk.Button(text="Click me")
btn1 = ttk.Button(text="Click me")

# btn.pack(fill = 'both', expand=True) - заполнение элемента на весь экран
# btn.pack(anchor="nw", padx=20, pady=30) - отступы виджета от границ контейнера
# btn.pack(side=LEFT, fill=Y)
btn.place(height=53, width=100)
# Параметр anchor помещает виджет в определенной части контейнера. Может принимать следующие значения:
#
# n: положение вверху по центру
#
# e: положение в правой части контейнера по центру
#
# s: положение внизу по центру
#
# w: положение в левой части контейнера по центру
#
# nw: положение в верхнем левом углу
#
# ne: положение в верхнем правом углу
#
# se: положение в нижнем правом углу
#
# sw: положение в нижнем левом углу
#
# center: положение центру

root.mainloop()