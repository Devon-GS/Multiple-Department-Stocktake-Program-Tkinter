from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
import muffin_stocktake

# Root window
root = Tk()
root.title('Sasol De Bron - Stock Count')
root.iconbitmap('icons/muffin_icon.ico')
root.geometry('435x225')

# Root window buttons
muffin_window = Button(root, text='Muffin Stock Take', command=muffin_stocktake.muffin_stock_take)
muffin_window.grid(row=0, column=0)

# Exit Button
exit_btn = Button(root, text='Exit', command=root.quit)
exit_btn.grid(row=3, column=0, columnspan=3, sticky=W+E, pady=(10, 0), padx=(5, 0))

# Run program
root.mainloop()