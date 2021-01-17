from tkinter import *
from tkinter import ttk


class Popup:
    def __init__(self):
        self.dialog = Tk()
        self.dialog.geometry('60x90')
        choices = ["Bubble Sort", "Insertion Sort", "Selection Sort"]
        self.label_com = Label(self.dialog, text='Sorting algorithm: ', padx=10)
        self.combobox = ttk.Combobox(self.dialog, values=choices, state='readonly', width=13)
        self.combobox.current(0)
        self.submit = Button(self.dialog, text='Submit', command=self.on_submit)
        
        self.label_com.grid(row=0, column=0, pady=3)
        self.combobox.grid(row=1, column=0, pady=1)
        self.submit.grid(row=2, column=0, pady=3) 
        self.choice = None
        self.dialog.update()
        self.position_dialog()
        self.dialog.mainloop()

        

    def position_dialog(self):
        # :position_dialog - position window in screen center
        screen_width = self.dialog.winfo_screenwidth()
        screen_height = self.dialog.winfo_screenheight()
        x = int(screen_width/2 - 60/2) 
        y = int(screen_height/2 -90/2)
        self.dialog.geometry(f'{60}x{90}+{x}+{y}')

    def on_submit(self):
        # :on_submit - submit button event
        self.choice = self.combobox.get()
        self.dialog.destroy()