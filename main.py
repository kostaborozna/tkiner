
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")

        # add widgets to app
        self.button = customtkinter.CTkButton(self, command=self.button_click, text="Число фиабоба")
        self.button.grid(row=0, column=0, padx=20, pady=10)

    # add methods to app
    def button_click(self):
        a = 0
        b = 1
        a, b = b, a + b

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app = App()
app.mainloop()