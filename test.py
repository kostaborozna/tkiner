import tkinter
import customtkinter



class Frame(customtkinter.CTkFrame):
    def __int__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

class App(customtkinter.CTk):
    def __int__(self):
        super().__init__()
        self.geometry("1200x800")
        self.title("First task")

        self.frame = Frame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")



# Change a theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = App()
app.mainloop()