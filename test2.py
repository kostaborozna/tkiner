import tkinter as tk


def calculate_sum():
    # Инициализируем сумму значением 0
    total = 0

    # Перебираем все чекбоксы и суммируем их значения, если они отмечены
    for checkbox, value in checkboxes:
        if checkbox.get():
            total += value

    # Обновляем текст в label
    result_label.config(text=f"Сумма: {total}")


# Создаем главное окно
root = tk.Tk()
root.title("Сумма чекбоксов")

# Создаем чекбоксы и их значения
checkboxes = []
values = [1, 2, 4, 8, 16]

for value in values:
    checkbox = tk.BooleanVar()
    checkbox.set(False)
    checkboxes.append((checkbox, value))

# Создаем и размещаем чекбоксы на форме
for i, (checkbox, value) in enumerate(checkboxes):
    checkbox_label = tk.Label(root, text=f"{value}")
    checkbox_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    checkbox_widget = tk.Checkbutton(root, variable=checkbox, command=calculate_sum)
    checkbox_widget.grid(row=i, column=1, padx=10, pady=5, sticky="w")

# Создаем и размещаем label для вывода результата
result_label = tk.Label(root, text="Сумма: 0")
result_label.grid(row=len(values), column=0, columnspan=2, padx=10, pady=5)

# Запускаем главный цикл
root.mainloop()
