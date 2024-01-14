import tkinter as tk
from tkinter import ttk

class OOP():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("เส้นใหญ่")
        self.createWidgets()

    def createWidgets(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab1, text="เส้นตรง")
        tabControl.add(tab2, text="วงกลม")
        tabControl.pack(expand=1, fill="both")

        lineHead = ttk.Labelframe(tab1, text='เลือกไฟล์')
        lineHead.grid(column=0, row=0, padx=8, pady=4)
        ttk.Label(lineHead,text="input file").grid(column=0, row=0, sticky='W')

        cirHead = ttk.Labelframe(tab2, text='เลือกไฟล์')
        cirHead.grid(column=0, row=0, padx=8, pady=4)
        ttk.Label(cirHead,text="input file").grid(column=0, row=0, sticky='W')

oop = OOP()
oop.win.mainloop()  # สั่งเปิดหน้าต่างโปรแกรม