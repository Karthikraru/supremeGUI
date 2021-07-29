import tkinter
from peewee import *
import datetime

db = SqliteDatabase('inventory.db')

class Entry(Model):
    name = TextField()
    size = FloatField(max_length=4)
    purchaseCost = FloatField(max_length=7)
    soldCost = FloatField(max_length=7)
    purchaseDate = DateTimeField()
    soldDate = DateTimeField()
    soldLocation = TextField()
    class Meta:
        database=db



class test:
    def __init__(self, master):
        self.master = master
        self.main = tkinter.LabelFrame(self.master, background='light grey', width=1000, height=1000)
        self.main.pack(fill=tkinter.BOTH, expand=True)

        self.build_grid()
        self.build_buttons()
        self.build_logo()

    def build_grid(self):
        self.main.columnconfigure(0, weight=0)
        self.main.columnconfigure(1, weight=0)
        self.main.columnconfigure(2, weight=0)
        self.main.rowconfigure(0, weight=0)
        self.main.rowconfigure(1, weight=0)
        self.main.rowconfigure(2, weight=0)
        self.main.rowconfigure(3, weight=0)

    def build_logo(self):
        logo = tkinter.Label(self.main, background='grey', foreground='white', text='Inventory Tracker', font=(40))
        logo.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

    def build_buttons(self):
        self.addPageButton = tkinter.Button(self.main, bg='light grey', text=' Add Inventory', command=self.addPage)
        self.addPageButton.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        self.viewInventoryButton = tkinter.Button(self.main, bg='light grey', text='View Inventory', command=self.inventoryPage)
        self.viewInventoryButton.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)

    def addPage(self):
        addPage = tkinter.Toplevel(background='light grey')
        logo = tkinter.Label(addPage, background='grey', foreground='white', text='Inventory Tracker', font=(40))
        logo.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)

    def inventoryPage(self):
        inventoryPage = tkinter.Toplevel(background='light grey')
        logo = tkinter.Label(inventoryPage, background='grey', foreground='white', text='Inventory Tracker', font=(40))
        logo.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)




if __name__ == '__main__':
    root = tkinter.Tk()
    test(root)
    root.mainloop()
