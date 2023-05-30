from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
from os import path
import database as db
from muffin_st import muffin_stocktake as muffin
from ingredients_st import ingredients_stocktake as ing

# --------------------------------------------------------------------------------
#   Things to do:
#           Move database reset to database file 
#           Move Functions to separate files
#           Sales including waste note (muffin and ingredients)
#           Add coffee stock take for ciro and lavazza
#           Cup and lid stock take for ciro and lavazza
# --------------------------------------------------------------------------------
#   Version: 3    
#   Add ingredients window 
#   Add ingredients buy window with labels and input
#   Add database init button and function to root window
#   Add on program run checker to see if database exists auto create if false
# --------------------------------------------------------------------------------
#   Version 4:
#   Changed database name to stock.db
#   Add database functionality to ingredients_st_buy   
#   Add buttons (Sales, stock take, view stock, Reset and exit) to ingrediends_st
#   Changed ingredients_st_buy to ingredients_st_func
#   Add frames to sale functon for ingredients
#   Add ingredientsSales table to database and update database.py 
# --------------------------------------------------------------------------------


# Root window
root = Tk()
root.title('Sasol De Bron - Stock Count')
root.iconbitmap('icons/muffin_icon.ico')
root.geometry('435x225')

# Root window butons
muffin_window = Button(root, text='Muffin Stock Take', command=muffin)
muffin_window.grid(row=0, column=0)

ingredients_window = Button(root, text='Ingredients Stock Take', command=ing)
ingredients_window.grid(row=1, column=0)

# Reset database button
initialize_database = Button(root, text='Reset Database', command=db.reset)
initialize_database.grid(row=2, column=0)


# On progeam run check for data base
file = path.exists('database/stock.db')
if not file:
    database_label = Label(root, text='Database not found! One was created for you')
    database_label.grid(row=3, column=0, sticky=W, pady=(10, 0), padx=(5, 0))
    db.database_init()

# Exit Button
exit_btn = Button(root, text='Exit', command=root.quit)
exit_btn.grid(row=5, column=0, columnspan=3, sticky=W+E, pady=(10, 0), padx=(5, 0))

# Run program
root.mainloop()