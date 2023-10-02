from passwordchecker import password_check

import tkinter
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('900x600')
        self.title('Custom ttk')

        # First task
        # Create frame
        self.button_frame_1 = customtkinter.CTkFrame(self, fg_color='#62b388')
        self.button_frame_1.grid(row=0, column=0, ipady=10,  padx=10, pady=20, sticky='nw')

        # Create label to frame
        self.label_1 = customtkinter.CTkLabel(self.button_frame_1, text='Числа Фибанначи')
        self.label_1.grid(row=0, column=0, padx=10, pady=10)

        # Create button
        self.button_1 = customtkinter.CTkButton(self.button_frame_1, text='Клик', command=self.next_number)
        self.button_1.grid(row=1, column=0,  padx=10, pady=10)

        # Magick numbers -__-
        self.fibanachi_fist = 0
        self.fibanachi_second = 1

        # Second task
        # Create frame
        self.second_task_frame = customtkinter.CTkFrame(self, fg_color='#62b388')
        self.second_task_frame.grid(row=0, column=1, ipady=10, padx=10, pady=20, sticky='n')

        # Create label to frame
        text_exp = ('Не судите, да не судимы будете, ибо каким судом судите,\n'
                    ' таким будете судимы и какою мерою мерите,\n'
                    ' такою и вам будут мерить')
        self.label_gospel = customtkinter.CTkLabel(self.second_task_frame, text=text_exp)
        self.label_gospel.grid(row=0, column=0, padx=10, pady=10)

        # Entry for user password
        self.password_entry = customtkinter.CTkEntry(self.second_task_frame, placeholder_text='Введите пароль для входа в рай')
        self.password_entry.grid(row=1, column=0, ipadx=60, padx=10, pady=10)

        self.button_entry = customtkinter.CTkButton(self.second_task_frame, text='Проверка на прочность',
                                                    command=self.button_second_task)
        self.button_entry.grid(row=2, column=0, ipadx=60, padx=10, pady=10)

        # Label for cool password system!!!
        self.label_update = customtkinter.CTkLabel(self.second_task_frame, text='')
        self.label_update.grid(row=3, column=0, ipadx=60, padx=10, pady=10)

        # Third task
        # Create frame
        self.third_task_frame = customtkinter.CTkFrame(self, fg_color='#62b388')
        self.third_task_frame.grid(row=0, column=2, padx=10, pady=20, sticky='ne')

        # TODO
        # # Create a checks (не получолось с for)
        # counter = 1
        # for i in range(5):
        #     self.check_button_1 = customtkinter.CTkCheckBox(self.third_task_frame, text=str(counter),
        #                                                     command=self.check_box_task)
        #     self.check_button_1.grid(row=i, column=0, ipadx=60, padx=10, pady=10)
        #     counter *= 2

        self.check_button_1 = customtkinter.CTkCheckBox(self.third_task_frame, text='1', command=self.check_box_task)
        self.check_button_1.grid(row=0, column=0, ipadx=60, padx=10, pady=10)
        self.check_button_2 = customtkinter.CTkCheckBox(self.third_task_frame, text='2', command=self.check_box_task)
        self.check_button_2.grid(row=1, column=0, ipadx=60, padx=10, pady=10)
        self.check_button_3 = customtkinter.CTkCheckBox(self.third_task_frame, text='4', command=self.check_box_task)
        self.check_button_3.grid(row=2, column=0, ipadx=60, padx=10, pady=10)
        self.check_button_4 = customtkinter.CTkCheckBox(self.third_task_frame, text='8', command=self.check_box_task)
        self.check_button_4.grid(row=3, column=0, ipadx=60, padx=10, pady=10)
        self.check_button_5 = customtkinter.CTkCheckBox(self.third_task_frame, text='16', command=self.check_box_task)
        self.check_button_5.grid(row=4, column=0, ipadx=60, padx=10, pady=10)

        # Label for result of sum
        self.label_result = customtkinter.CTkLabel(self.third_task_frame, text='Сумма')
        self.label_result.grid(row=5, column=0, ipadx=60, padx=10, pady=10)

        # Fourth task
        # Create frame
        self.fourth_task_frame = customtkinter.CTkFrame(self, fg_color='#62b388')
        self.fourth_task_frame.grid(row=1, column=1, padx=10, sticky='n')

        self.radio_var = tkinter.IntVar(value=0)

        self.radio_button_1 = customtkinter.CTkRadioButton(self.fourth_task_frame, text='List',
                                                           variable=self.radio_var, value=1, command=self.radio_button_checks)
        self.radio_button_1.grid(row=0, column=0, ipadx=60, padx=10, pady=10)
        self.radio_button_2 = customtkinter.CTkRadioButton(self.fourth_task_frame, text='Dictonary',
                                                           variable=self.radio_var, value=2, command=self.radio_button_checks)
        self.radio_button_2.grid(row=1, column=0, ipadx=60, padx=10, pady=10)
        self.radio_button_3 = customtkinter.CTkRadioButton(self.fourth_task_frame, text='Sets',
                                                           variable=self.radio_var, value=3, command=self.radio_button_checks)
        self.radio_button_3.grid(row=2, column=0, ipadx=60, padx=10, pady=10)

        self.label_radio_buttons = customtkinter.CTkLabel(self.fourth_task_frame, text='Пример')
        self.label_radio_buttons.grid(row=3, column=0, ipadx=60, padx=10, pady=10, sticky='ns')


    # Methods for buttons and another shit
    def next_number(self):
        self.fibanachi_fist, self.fibanachi_second = self.fibanachi_second, self.fibanachi_fist + self.fibanachi_second
        self.button_1.configure(text=str(self.fibanachi_second))

    def button_second_task(self):
        checks = str(self.password_entry.get())
        result = password_check(checks)
        self.label_update.configure(text=str(result))

    def check_box_task(self):
        total = 0
        if self.check_button_1.get():
            total += int(self.check_button_1.cget('text'))
        if self.check_button_2.get():
            total += int(self.check_button_2.cget('text'))
        if self.check_button_3.get():
            total += int(self.check_button_3.cget('text'))
        if self.check_button_4.get():
            total += int(self.check_button_4.cget('text'))
        if self.check_button_5.get():
            total += int(self.check_button_5.cget('text'))
        self.label_result.configure(text=f'Сумма: {total}')

    def radio_button_checks(self):
        if self.radio_var.get() == 1:
            self.label_radio_buttons.configure(text='numbers = [1, 2, 3]\nnumbers[0] = 4\nnumbers.append(5)')
        elif self.radio_var.get() == 2:
            self.label_radio_buttons.configure(text='person = {"name": "Alice", "age": 30}\nperson = {"name": "Alice", "age": 30}'
                                                    '\nperson["city"] = "New York"')
        elif self.radio_var.get() == 3:
            self.label_radio_buttons.configure(text='colors = {"red", "green", "blue"}\ncolors.add("yellow")\ncolors.remove("red")')

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')
app = App()
app.mainloop()