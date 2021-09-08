from tkinter import ttk, messagebox
import tkinter as tk
import subprocess
import os
class Demo2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.entry1 = tk.Entry(self)
        self.b2 = tk.Button(self, text="MAC Değiştir", bg='black', fg='#469A00',command=lambda:self.mac_changer(str(self.entry1.get())))
        self.entry1.grid(row=0, column=1)
        self.b2.grid(row=0, column=5)
        self.b2.place(x=80, y=50)
        self.entry1.place(x=80, y=15)
    def mac_changer(self,mac):
        try:
            self.command = ("macchanger -r %s" % (mac))
            os.popen(self.command)
        except:
            print("NO")

app = Demo2()
app.geometry("300x100")
app.mainloop()
